from os import listdir, mkdir, rename
from os.path import join, exists, isdir

from git import Repo, GitCommandError

from model.assignment import Assignment


class Student:
    directory_name = 'assignment'

    def __init__(self, student_id, name, repo):
        self.id = str(student_id)
        self.name = name
        self.repo = repo
        if not isdir(Student.directory_name):
            mkdir(Student.directory_name)

        self.dir = join(Student.directory_name, self.id)
        self.assignments = {}
        self.score = {week: -1 for week in Assignment.assignment_list}  # 미제출 시 -1점

    @classmethod
    def create(cls, df):
        student = Student(
            student_id=df['학번'],
            name=df['이름'],
            repo=df['repo']
        )
        return student

    def clone_repo(self):
        if exists(self.dir):
            return

        mkdir(self.dir)
        try:
            Repo.clone_from(self.repo, self.dir)
        except GitCommandError:
            print(self.id, self.name, self.repo, 'repository 문제')

    def test_assignment(self, assignment_id):
        try:
            self.assignments[assignment_id].run_test()
            self.score[assignment_id] = self.assignments[assignment_id].check_score()
        except KeyError:
            print(assignment_id, 'Test Key Error')

    def test_all(self):
        for week in Assignment.assignment_list:
            self.test_assignment(week)

    def rename_folder(self):
        if 'OOP' in listdir(self.dir):
            self.dir = join(self.dir, 'OOP')
        for directory_name in listdir(self.dir):
            path = None
            directory_path = join(self.dir, directory_name)
            if '12' in directory_name:
                path = join(self.dir, 'week12')
            elif '11' in directory_name:
                path = join(self.dir, 'week11')
            elif '10' in directory_name:
                path = join(self.dir, 'week10')
            elif '10_' in directory_name:
                path = join(self.dir, 'week10_')
            elif '7' in directory_name:
                path = join(self.dir, 'week7')
            elif '4' in directory_name:
                path = join(self.dir, 'week4')
            elif '3' in directory_name:
                path = join(self.dir, 'week3')
            elif '2' in directory_name and '12' not in directory_name:
                path = join(self.dir, 'week2')
            elif '1' in directory_name and '11' not in directory_name and '10' not in directory_name:
                path = join(self.dir, 'week1')
            elif 'mid' in directory_name or 'MT' in directory_name:
                path = join(self.dir, 'midterm')

            if not path:
                return

            if 'ex' not in directory_name.lower() and 'prac' not in directory_name.lower():
                rename(directory_path, path)

    def update_assignment(self):

        for directory_name in listdir(self.dir):
            directory_path = join(self.dir, directory_name)

            if directory_name.startswith('.') or not isdir(directory_path) or not directory_name.startswith('week'):
                continue

            try:
                assignment = Assignment.create(directory_name, directory_path)
                self.assignments[directory_name] = assignment
            except KeyError:
                print(self.id, self.name, ' 파일이름 에러:', self.dir, directory_name)
