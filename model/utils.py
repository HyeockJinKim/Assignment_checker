
def read_all_file(path):
    with open(path, 'r') as f:
        contents = f.readlines()

    return '\n'.join(contents)
