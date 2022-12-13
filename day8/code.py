# rows = [list(map(int, line)) for line in open('day8/test.txt').read().splitlines()]
rows = [list(map(int, line)) for line in open('day8/data.txt').read().splitlines()]


def compute_max_left_right(trees, visibility_matrix, transposed):
    for y, row in enumerate(trees):
        max_x = -1
        for x, val in enumerate(row):
            if val > max_x:
                visibility_matrix[y if not transposed else x][x if not transposed else y] = 1
                max_x = val

        max_x = -1
        for x, val in enumerate(reversed(row)):
            x = len(row) - 1 - x
            if val > max_x:
                visibility_matrix[y if not transposed else x][x if not transposed else y] = 1
                max_x = val


def part1():
    visibility_matrix = [[0 for i in range(len(rows[0]))] for j in range(len(rows))]

    compute_max_left_right(rows, visibility_matrix, False)
    compute_max_left_right([list(map(int, col)) for col in zip(*rows)], visibility_matrix, True)
    return sum(list(map(sum, visibility_matrix)))


def compute_neighbours(x, y):
    # FIXME: to be implemented
    return 0

def part2():
    max_view = -1
    for y in range(1, len(rows)-1):
        for x in range(1, len(rows[0])-1):
            total = compute_neighbours(x, y)
            if total > max_view:
                max_view = total

    return max_view

