data = open("day1.txt", "r").read().replace("\n\n", ",").replace("\n", "+")[:-1]

def part1():
    return max(map(eval, data.split(',')))


def part2():
    sorted_lines = list(map(eval, data.split(',')))
    sorted_lines.sort()
    return sum(sorted_lines[-3:])



