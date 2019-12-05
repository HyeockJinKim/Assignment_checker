import os

import pandas as pd

from checker.namer import name_to_csv
from model.student import Student


class Classes:
    def __init__(self, students):
        self.students = students

    @classmethod
    def create(cls, csv_file='checker.csv'):
        if not os.path.exists(csv_file):
            name_to_csv(csv_file)
        df = pd.read_csv(csv_file, encoding='utf-8')
        df = df.fillna('')

        students = [Student.create(row) for i, row in df.iterrows()]
        classes = Classes(students)
        return classes

    def clone_all(self):
        print('Clone repository :: \n')

        # length = len(self.students)
        student = self.students[1]
        student.clone_repo()
        student.rename_folder()

        # for i, student in enumerate(self.students):
        #     student.clone_repo()
        #     student.rename_folder()
        #     print('진행 상황: ', i, '/', length)
        print()

    def test_all(self):
        print('Test code Run :: \n')

        # length = len(self.students)
        student = self.students[1]
        student.test_all()
        # for i, student in enumerate(self.students):
        #     student.test_all()
        #     print('진행 상황: ', i, '/', length)
        print()

    def update_all(self):
        print('Read Assignment :: \n')

        # length = len(self.students)
        student = self.students[1]
        student.update_assignment()
        # for i, student in enumerate(self.students):
        #     student.update_assignment()
        #     print('진행 상황: ', i, '/', length)
        print()

    def score_all(self):
        print('Show Score :: \n')
        student = self.students[1]
        print(student.id, student.name, student.score)
        # for i, student in enumerate(self.students):
        #     print(student.id, student.name, student.score)
        print()
