def print_day1_1():
    f = open("day1.txt", "r")
    lines = f.readlines()
    print(f'day1_1: {max(map(eval, lines))}')

def print_day1_2():
    f = open("day1.txt", "r")
    lines = f.readlines()
    sorted = list(map(eval, lines))
    sorted.sort()
    print(f'day1_2:, {sum(sorted[-3:])}')

if __name__ == '__main__':
    print_day1_1()
    print_day1_2()
