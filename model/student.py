import os

from git import Repo, GitCommandError


class Student:
    directory_name = 'assignment'

    def __init__(self, student_id, name, repo):
        self.id = str(student_id)
        self.name = name
        self.repo = repo
        self.dir = os.path.join(Student.directory_name, self.id)

    def update_assignment(self):
        pass

    def clone_repo(self):
        if os.path.exists(self.dir):
            return

        os.mkdir(self.dir)
        try:
            repo = Repo.clone_from(self.repo, self.dir)
        except GitCommandError as e:
            print(self.id, self.name, self.repo, 'repository 문제')
