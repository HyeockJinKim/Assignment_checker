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
        length = len(self.students)
        for i, student in enumerate(self.students):
            student.clone_repo()
            print('진행 상황: ', i, '/', length)

    def test_all(self):
        length = len(self.students)
        for i, student in enumerate(self.students):
            student.test_all()
            print('진행 상황: ', i, '/', length)

    def update_all(self):
        length = len(self.students)
        for i, student in enumerate(self.students):
            student.update_assignment()
            print('진행 상황: ', i, '/', length)
