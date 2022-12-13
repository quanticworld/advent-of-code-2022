import re

from anytree import PreOrderIter
from numpy import sort
from common.nodes import FileNode

# data = open("day7/test.txt", "r").read().splitlines()[1:]  # test data
data = open("day7/data.txt", "r").read().splitlines()[1:]


def part1():
    root = fill_tree()
    total = 0
    for node in PreOrderIter(root):
        total += node.sum_children if node.sum_children < 100000 else 0
    return total


def part2():
    root = fill_tree()
    filled = root.sum_children
    available = 70000000 - filled
    needed = 30000000 - available
    size_to_delete = list(filter(lambda x: x > needed, sort(list(map(lambda n: n.sum_children, list(PreOrderIter(root)))))))[0]
    return size_to_delete


def fill_tree():
    root = FileNode('/', 0, 0, None, [])
    parent = root
    current_depth = 1
    for row in data:
        while parent.parent and current_depth <= parent.depth:
            parent = parent.parent

        if row[0:4] == '$ ls':
            continue
        elif row[0:4] == 'dir ':
            continue
        elif row[0:7] == '$ cd ..':
            current_depth -= 1
            continue
        elif row[0:5] == '$ cd ':
            parent = FileNode(row[5:], 0, 0, parent.parent if current_depth == parent.depth else parent)
            current_depth += 1
        else:
            parsed_info = re.search('^([0-9]+) (.*)', row)
            FileNode(parsed_info.group(2), int(parsed_info.group(1)), 0, parent, [])
            parent_for_sum = parent
            while parent_for_sum is not None:
                parent_for_sum.sum_children += int(parsed_info.group(1))
                parent_for_sum = parent_for_sum.parent
    return root


