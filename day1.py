import timeit


def print_day1_1():
    f = open("day1.txt", "r")
    lines = f.readlines()
    return max(map(eval, lines))


def print_day1_2():
    f = open("day1.txt", "r")
    lines = f.readlines()
    sorted_lines = list(map(eval, lines))
    sorted_lines.sort()
    return sum(sorted_lines[-3:])


if __name__ == '__main__':
    num_runs = 1000
    day1_time = timeit.Timer(print_day1_1).timeit(num_runs) / num_runs * 1000
    day2_time = timeit.Timer(print_day1_2).timeit(num_runs) / num_runs * 1000

    pretty_print_table = \
        [
            ['part', 'result', f'avg (ms) / {num_runs} iterations'],
            ['----------', '----------', '-------------------------'],
            ['day1_1', print_day1_1(), round(day1_time, 6)],
            ['day1_2', print_day1_2(), round(day2_time, 6)],
        ]
    for row in pretty_print_table:
        print('| {:^10} | {:>10} | {:>25} |'.format(*row))
