#! /usr/bin/env python3

import re

from collections import defaultdict


def read_input(filename="input.txt"):
    with open(filename, "r") as f:
        data = f.readlines()
    return data


def scan_lines(data):
    board = defaultdict(int)
    for d in data:
        m = re.match(r"^(\d+),(\d+) -> (\d+),(\d+)$", d)
        x1 = int(m.group(1))
        y1 = int(m.group(2))
        x2 = int(m.group(3))
        y2 = int(m.group(4))
        if x1 == x2:
            y = min(y1, y2)
            while y <= max(y1, y2):
                board[f"{x1},{y}"] += 1
                y += 1
        elif y1 == y2:
            x = min(x1, x2)
            while x <= max(x1, x2):
                board[f"{x},{y1}"] += 1
                x += 1

    return board


def main():
    data = read_input("input.txt")
    board = scan_lines(data)
    return sum(1 for x in board.values() if x > 1)


if __name__ == "__main__":
    result = main()
    print(result)
