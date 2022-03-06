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

def show_items(item_dict):
    for key, value in item_dict.items():
        print(key, value+'yen')

def assign_item_id(item_dict):
    id_to_item = {}
    for num, key in enumerate(item_dict.keys()):
        id_to_item[num] = key
    print(id_to_item)


def main(args):
    item_file = args.item_file

    # Read items as dictionary formula.
    item_dict = read_item_list(item_file)
    show_items(item_dict)
    assign_item_id(item_dict)

    # input loop
    while True:
        inp = input('')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--item_file', type=str, default='/Users/mishizuka/git/pos/data/items.csv')
    args = parser.parse_args()
    main(args)