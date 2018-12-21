from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('--great', help='make it great', action='store_true')
parser.add_argument('--awesome', help='make it awesome', action='store_true')

args = parser.parse_args()

if args.great:
    print('a great big hello world!')
elif args.awesome:
    raise NotImplementedError()
else:
    print('hello world!')
