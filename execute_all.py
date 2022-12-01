import timeit
import day1

if __name__ == '__main__':
    num_runs = 1000
    day1_time = timeit.Timer(day1.part1).timeit(num_runs) / num_runs * 1000
    day2_time = timeit.Timer(day1.part2).timeit(num_runs) / num_runs * 1000

    pretty_print_table = \
        [
            ['part', 'result', f'avg (ms) / {num_runs} iter'],
            ['----------', '----------', '--------------------'],
            ['day1_1', day1.part1(), round(day1_time, 6)],
            ['day1_2', day1.part2(), round(day2_time, 6)],
        ]
    for row in pretty_print_table:
        print('| {:^10} | {:>10} | {:>20} |'.format(*row))
