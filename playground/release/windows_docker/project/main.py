import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Demo Application')
    parser.add_argument("-n", "--name-val", help='This will be printed on console', default='default')
    args, unknown = parser.parse_known_args()
    if unknown:
        print('Invalid command args')
    if args:
        print(f' Args passed is {args.name_val}')
