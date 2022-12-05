from utils import init_list_of_objects

# data = open("day5/test.txt", "r").read().splitlines()  # test data
data = open("day5/data.txt", "r").read().splitlines()


def part1():
    return execute(False)


def part2():
    return execute(True)


def execute(keep_order):
    stacks = init_list_of_objects(int((len(data[0]) + 1) / 4))
    for row in data:
        if row and (row[0] == '[' or row[0] == ' ') and row[0:2] != ' 1':
            add_stack(row, stacks)
        elif row.startswith("move"):
            process(row, stacks, keep_order)
    return ''.join([x.pop() for x in filter(lambda s: len(s) > 0, stacks)])


def add_stack(row, stacks):
    row = [row[i+1:i+2] for i in range(0, len(row), 4)]
    for idx, elem in enumerate(row):
        if elem != ' ':
            stacks[idx].insert(0, elem)


def process(row, stacks, keep_order):
    row = row.replace('move ', '').replace(' from ', ',').replace(' to ', ',').split(',')
    quantity, from_row, to_row = int(row[0]), int(row[1]) - 1, int(row[2]) - 1

    if keep_order:
        stacks[to_row].extend(stacks[from_row][-quantity:])
        del stacks[from_row][-quantity:]
    else:
        for i in range(0, quantity):
            stacks[to_row].extend(stacks[from_row].pop())
