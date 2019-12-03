import os
import subprocess


def make_cpp(content):
    c_file = 'tester_code.cpp'
    if not os.path.exists(c_file):
        with open(c_file, 'w') as f:
            f.write(content)

    execution_file = 'tester_code'
    compile_res = subprocess.call(['gcc', '-o', execution_file, c_file], stderr=subprocess.DEVNULL)
    print(compile_res)
    if compile_res == 1:
        return compile_res

    run_res = subprocess.call(execution_file)
    print(run_res)
    return compile_res, run_res

