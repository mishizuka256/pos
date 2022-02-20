import argparse
import json
from pathlib import Path


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
    print(item_dict)
    print(item_dict['brend_coffee_L'])
    print(item_dict['brend_coffee_M'])
    print(item_dict['brend_coffee_S'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--item_file', type=str, default='/Users/mishizuka/git/pos/data/items.csv')
    args = parser.parse_args()
    main(args)