import sys
import os

if __name__ == '__main__':
    p = os.popen('git rev-list --tags --max-count=1')
    commit = p.read()
    p.close()

    p = os.popen(f'git describe --tags {commit}')
    tag = p.read()
    p.close()

    # print('get tag:', tag)

    version = str(tag[1:])
    version_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../QtScrcpy/version"))
    with open(version_file, 'w') as file:
        file.write(version)
    sys.exit(0)