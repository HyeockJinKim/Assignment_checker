from model.test_code import TestCode


class Assignment:
    assignment_dict = {
        # default
        'week2': 'week2',
        'week3': 'week3',
        'week4': 'week4',
        'week7': 'week7',
        'week10': 'week10',
        'week11': 'week11',
        'week12': 'week12',
        'midterm': 'midterm',

        # special case
        'OOP-2': 'week2',
        'OOP-3': 'week3',

        'week_2': 'week2',
        'week_3': 'week3',
        'week_4': 'week4',
        'week_7': 'week7',
        'week_10': 'week10',
        'week_11': 'week11',
        'week_12': 'week12',
    }
    test_case = {week: [] for week in assignment_dict.values()}

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

    @classmethod
    def add_test_case(cls, assignment_id, header, body, cmd=None):
        try:
            cls.test_case[assignment_id].append(TestCode.create(assignment_id, header, body, cmd))
        except KeyError:
            print('No key :', assignment_id)

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
        s = 0
        for score in self.score:
            s += score['compile_res'] * 40
            s += score['run_res'] * 60

        return s / length
