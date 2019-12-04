import subprocess
from os.path import join, exists


class TestCode:
    DEFAULT_CPP_FILE = 'test_code.cpp'
    DEFAULT_RUN_FILE = 'test_run_file'

    def __init__(self, assignment_id, header, body, cmd=None):
        self.assignment_id = assignment_id
        self.header = header
        self.body = body
        self.cmd = cmd

    @classmethod
    def create(cls, assignment_id, header, body, cmd=None):
        test_code = TestCode(
            assignment_id=assignment_id,
            header=header,
            body=body,
            cmd=cmd
        )
        return test_code

    @classmethod
    def default_gpp_cmd(cls, test_file, execution_file):
        return ['gcc', '-o', execution_file, test_file]

    @classmethod
    def write_test_code(cls, content, file_path):
        if not exists(file_path):
            with open(file_path, 'w') as f:
                f.write(content)

    @classmethod
    def compile_test_code(cls, test_file, execution_file, cmd=None):
        if not cmd:
            cmd = cls.default_gpp_cmd(test_file, execution_file)

        compile_res = subprocess.call(cmd, stderr=subprocess.DEVNULL)
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
        file_path = join(directory_path, self.DEFAULT_CPP_FILE)
        execution_file = join(directory_path, self.DEFAULT_RUN_FILE)

        content = [self.header, 'int main() {', self.body, '    return 0;', '}']
        return self.test_full_code('\n'.join(content), file_path, execution_file, self.cmd)
