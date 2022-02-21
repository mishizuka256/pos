import argparse
import json
from pathlib import Path


# Convert menu items in input file to dictionary.
def read_item_list(item_file):
    file_contents = open(item_file, 'r')
    item_list = []
    item_dict = {}
    for line in file_contents:
        item_list.append(line.strip().split(','))
    for item in item_list:
        item_dict[item[1]] = item[2]
    print(item_dict)

    return item_dict


def main(args):
    item_file = args.item_file

    item_dict = read_item_list(item_file)
    for key, value in item_dict.items():
        print(key, value+'yen')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--item_file', type=str, default='/Users/mishizuka/git/pos/data/items.csv')
    args = parser.parse_args()
    main(args)