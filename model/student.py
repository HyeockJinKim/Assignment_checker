from os import listdir, mkdir
from os.path import join, exists, isdir

from git import Repo, GitCommandError

from model.assignment import Assignment


class Student:
    directory_name = 'assignment'

    def __init__(self, student_id, name, repo):
        self.id = str(student_id)
        self.name = name
        self.repo = repo
        self.dir = join(Student.directory_name, self.id)
        self.assignments = {}
        self.score = {}

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
            self.score[assignment_id] = 0

    def test_all(self):
        for week in Assignment.assignment_dict.values():
            self.test_assignment(week)

    def update_assignment(self):
        for directory_name in listdir(self.dir):
            directory_path = join(self.dir, directory_name)
            if directory_name.startswith('.') or not isdir(directory_path):
                continue

            try:
                assign = Assignment.assignment_dict[directory_name.lower()]
                assignment = Assignment.create(assign, directory_path)
                self.assignments[assign] = assignment
            except KeyError:
                print(self.id, self.name, ' 파일이름 에러:', self.dir, directory_name)

