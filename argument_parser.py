import argparse


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