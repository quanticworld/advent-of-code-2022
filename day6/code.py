# data = open("day6/test.txt", "r").read().splitlines()[0]  # test data
data = open("day6/data.txt", "r").read().splitlines()[0]


def part1():
    return execute(4)


def part2():
    return execute(14)


def execute(code_length):
    i = 0
    while (True):
        if all(data[i:i+code_length].count(c) == 1 for c in data[i:i+code_length]):
            return i+code_length
        else:
            i += 1
