from os import listdir

from model.test_code import TestCode


class Assignment:
    assignment_list = ['week2', 'week3', 'week4', 'week5', 'week7', 'week10', 'week11', 'week12']
    test_case = {week: TestCode.list_test_case(TestCode.DEFAULT_TEST_PATH, week)
                 for week in listdir(TestCode.DEFAULT_TEST_PATH)}

    def __init__(self, assignment_id, directory):
        self.assignment_id = assignment_id
        self.dir = directory
        self.score = []

    @classmethod
    def create(cls, assignment_id, directory):
        assignment = Assignment(
            assignment_id=assignment_id,
            directory=directory
        )
        return assignment

    def run_test(self):
        try:
            test_list = self.test_case[self.assignment_id]
            for test_code in test_list:
                compile_res, run_res = test_code.test_cpp_template_code(self.dir)
                self.score.append({'compile_res': compile_res, 'run_res': run_res})
        except KeyError:
            self.score.append({'compile_res': False, 'run_res': False})
            print('No Test :', self.assignment_id)

    def check_score(self):
        length = len(self.score)
        if length == 0:
            return None  # Test code가 없음
        s = 0
        for score in self.score:
            if score['compile_res'] is not None:
                s += score['compile_res'] * 40
            if score['run_res'] is not None:
                s += score['run_res'] * 60
        return s / length
