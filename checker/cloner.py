import pandas as pd
from git import Repo, GitCommandError
import os


def clone_all(directory_name='assignment'):
    repos = []
    df = pd.read_csv('checker.csv', encoding='utf-8')
    df = df.fillna('')

    if not os.path.exists(directory_name):
        os.mkdir(directory_name)

    for i, row in df.iterrows():
        folder = os.path.join(directory_name, str(row['학번']))
        if os.path.exists(folder):
            repo = Repo(folder)
            repos.append(repo)
            continue

        os.mkdir(folder)
        try:
            repo = Repo.clone_from(row['repo'], folder)
            repos.append(repo)
        except GitCommandError as e:
            print(row['학번'], row['이름'], row['repo'], 'repository 문제')

    return repos
