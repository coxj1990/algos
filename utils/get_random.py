import os
import random
import argparse
from glob import glob

def get_basename(filename):
    return os.path.splitext(os.path.basename(filename))[0]

def is_algo(filename):
    basename = get_basename(filename)
    if basename == "__init__":
        return False
    dirname = os.path.dirname(filename)
    if "types" in dirname:
        return False
    if "utils" in dirname:
        return False
    return True

def get_filenames():
    return [y for x in os.walk("src") for y in glob(os.path.join(x[0], '*.py'))]

def get_algos():
    filenames = get_filenames()
    return [get_basename(f) for f in filenames if is_algo(f)]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--count', action='store_true')
    args = parser.parse_args()
    algos = get_algos()
    if args.count:
        print(len(algos))
    else:
        print(random.choice(algos))

if __name__ == '__main__':
    main()
