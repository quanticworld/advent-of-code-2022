rows = open('day13/test.txt').read().splitlines()
# rows = open('day13/data.txt').read().splitlines()

def flat(l):
    flat_list = []
    for element in l:
        if type(element) is list:
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list


def part1():
    for row in rows:
        print(row)
        print(flat(list))

    return 0


def part2():
    return 0

