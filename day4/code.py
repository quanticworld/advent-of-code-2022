from functools import reduce
from operator import add

# data = open("day4/test.txt", "r").read().splitlines()  # test data
data = open("day4/data.txt", "r").read().splitlines()


def make_range(s):
    x = set(range(*[int(b) + c for c, b in enumerate(s.split('-'))]))
    return x


def make_split_section(s):
    res = list(map(make_range, s.split(',')))
    return res


def part1():
    split_sections = list(map(make_split_section, data))
    is_fully_contained = list(map(lambda s: 1 if s[0].issubset(s[1]) or s[1].issubset(s[0]) else 0, split_sections))
    return reduce(add, is_fully_contained)


def part2():
    split_sections = list(map(make_split_section, data))
    overlap = list(map(lambda s: 1 if s[0] & s[1] else 0, split_sections))
    return reduce(add, overlap)

