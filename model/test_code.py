import subprocess
from os import listdir
from os.path import join, exists, isdir

from model.utils import read_all_file


class TestCode:
    DEFAULT_CPP_FILE = 'test_code.cpp'
    DEFAULT_RUN_FILE = 'test_run_file'
    DEFAULT_TEST_PATH = 'test_case'

    def __init__(self, assignment_id, header, body):
        self.assignment_id = assignment_id
        self.header = header
        self.body = body

    @classmethod
    def create(cls, assignment_id, header, body):
        test_code = TestCode(
            assignment_id=assignment_id,
            header=header,
            body=body,
        )
        return test_code

    @classmethod
    def list_test_case(cls, test_path, assignment_id):
        cases = []
        path = join(test_path, assignment_id)
        dirs = listdir(path)

        header_file = join(path, '.header')
        if exists(header_file):
            header = read_all_file(header_file)
        else:
            header = ''

        for t in dirs:
            if t.startswith('.'):
                continue
            test = join(path, t)
            body = read_all_file(test)
            test_case = cls.create(assignment_id, header, body)
            cases.append(test_case)

        return cases

    @classmethod
    def object_gpp_cmd(cls, test_file):
        return ['g++', '-o', test_file.replace('.cpp', '.o'), '-c', test_file]

    @classmethod
    def default_gpp_cmd(cls, test_file, execution_file):
        return ['g++', '-o', execution_file, test_file]

    @classmethod
    def default_make_cmd(cls, path):
        return ['make', '-C', path]

    @classmethod
    def write_test_code(cls, content, file_path):
        with open(file_path, 'w') as f:
            f.write(content)

    @classmethod
    def compile_test_code(cls, test_file, execution_file, cmd=None):
        if not cmd:
            cmd = cls.default_gpp_cmd(test_file, execution_file)

        compile_res = subprocess.call(cmd)
        print(compile_res, cmd)
        # compile_res = subprocess.call(cmd, stderr=subprocess.DEVNULL)
        # if '7' in test_file:
        #     print(test_file, execution_file, compile_res)

        return compile_res == 0

    @classmethod
    def run_test_code(cls, execution_file):
        return subprocess.call(execution_file) == 0

    @classmethod
    def test_full_code(cls, content, test_file, execution_file='out_file', cmd=None):
        cls.write_test_code(content, test_file)

        if not cls.compile_test_code(test_file, execution_file, cmd):
            return False, None

        run_res = cls.run_test_code(execution_file)
        return True, run_res

    def test_cpp_template_code(self, directory_path):
        if '7' in directory_path:
            if 'smart_obj' in listdir(directory_path):
                directory_path = join(directory_path, 'smart_obj')

            file_path = join(directory_path, self.DEFAULT_CPP_FILE)
            execution_file = join(directory_path, self.DEFAULT_RUN_FILE)

            smart_ptr = join(directory_path, 'smart_ptr')

            file_list = [join(smart_ptr, cpp) for cpp in listdir(smart_ptr) if cpp.endswith('.cpp')]
            file_list.append(file_path)
            for file in file_list:
                sub_cmd = self.object_gpp_cmd(file)
                subprocess.call(sub_cmd, stderr=subprocess.DEVNULL)

            file_list = list(map(lambda name: name.replace('.cpp', '.o'), file_list))
            cmd = self.default_gpp_cmd(' '.join(file_list), execution_file)
        else:
            file_path = join(directory_path, self.DEFAULT_CPP_FILE)
            execution_file = join(directory_path, self.DEFAULT_RUN_FILE)

            cmd = self.default_gpp_cmd(file_path, execution_file)

        content = [self.header, 'int main() {', self.body, '    return 0;', '}']
        return self.test_full_code('\n'.join(content), file_path, execution_file, cmd)
