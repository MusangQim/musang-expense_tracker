import argparse


# parent
parser = argparse.ArgumentParser()
# subparser
subparser = parser.add_subparsers()

# parse for 'ADD'
parser_add = subparser.add_parser('add')
parser_add.add_argument('--description')
parser_add.add_argument('--amount')

# parse for 'DELETE'
parser_del = subparser.add_parser('delete')
parser_del.add_argument('--id')

# parse for 'SUMMARY'
parser_sum = subparser.add_parser('summary')
parser_sum.add_argument('--month')

# parse for 'LIST'
parser_list = subparser.add_parser('list')

'''
parser.add_argument("add")
parser.add_argument("delete")
parser.add_argument("summary")
parser.add_argument("list")
'''

args = parser.parse_args()
print(args)

# print(f"{args.add}")
# print(f"{args.description}")
# print(f"{args.amount}")
# print(f"{args.delete}")
# print(f"{args.id}")
# print(f"{args.summary}")
# print(f"{args.month}")
# print(f"{args.list}")

# Learning Process about argparse
'''
parser = argparse.ArgumentParser()
parser.add_argument("nama")
args = parser.parse_args()
print(f"Hello, {args.nama}!")
'''

'''
parser = argparse.ArgumentParser()
parser.add_argument("nama")
parser.add_argument("--umur")
args = parser.parse_args()
print(F"Hello, {args.nama}")
if args.umur:
    print(f"Umur anda {args.umur} tahun.")
'''