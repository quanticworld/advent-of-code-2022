# A or X = 1 for Rock
# B or Y = 2 for Paper
# C or Z = 3 for Scissors

# 0 lost
# 3 draw
# 6 won

choice_dict = {'A': 1, 'X': 1, 'B': 2, 'Y': 2, 'C': 3, 'Z': 3}

# tuples : (part1 score, part2 strategy)
score_dict = {'A': {}, 'B': {}, 'C': {}}
score_dict['A']['X'] = (3, 'Z')
score_dict['A']['Y'] = (6, 'X')
score_dict['A']['Z'] = (0, 'Y')
score_dict['B']['X'] = (0, 'X')
score_dict['B']['Y'] = (3, 'Y')
score_dict['B']['Z'] = (6, 'Z')
score_dict['C']['X'] = (6, 'Y')
score_dict['C']['Y'] = (0, 'Z')
score_dict['C']['Z'] = (3, 'X')

games = open("day2/data.txt", "r").readlines()


def part1():
    total_score = 0
    for g in games:
        total_score += score_dict[g[0]][g[2]][0] + choice_dict[g[2]]
    return total_score


def part2():
    total_score = 0
    for g in games:
        choice = score_dict[g[0]][g[2]][1]
        total_score += score_dict[g[0]][choice][0] + choice_dict[choice]
    return total_score



