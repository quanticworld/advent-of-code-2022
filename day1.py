import timeit


def part1():
    f = open("day1.txt", "r")
    lines = f.readlines()
    return max(map(eval, lines))


def part2():
    f = open("day1.txt", "r")
    lines = f.readlines()
    sorted_lines = list(map(eval, lines))
    sorted_lines.sort()
    return sum(sorted_lines[-3:])



