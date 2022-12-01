import timeit


def part1():
    data = open("day1.txt", "r").read().replace("\n\n", ",").replace("\n", "+")[:-1]
    return max(map(eval, data.split(',')))

def part2():
    data = open("day1.txt", "r").read().replace("\n\n", ",").replace("\n", "+")[:-1]
    sorted_lines = list(map(eval, data.split(',')))
    sorted_lines.sort()
    return sum(sorted_lines[-3:])



