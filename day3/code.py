import textwrap
from functools import reduce
from operator import add
# data = open("day3/test.txt", "r").readlines()  # test data
data = open("day3/data.txt", "r").readlines()

mapping = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
    'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
    'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39,
    'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52,
}


def part1():
    split_bags = list(map(lambda x: textwrap.wrap(x, len(x) // 2), data))
    common_item_list = list(map(lambda bag: set(bag[0]).intersection(bag[1]).pop(), split_bags))
    return reduce(add, list(map(lambda x: mapping[x], common_item_list)))


def part2():
    split_bags = [data[i:i+3] for i in range(0, len(data), 3)]
    common_item_list = list(map(lambda bag: set(bag[0]).intersection(bag[1]).intersection(bag[2]).difference('\n').pop(), split_bags))
    return reduce(add, list(map(lambda x: mapping[x], common_item_list)))

