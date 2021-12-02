#! /usr/bin/env python3

class Submarine(object):

    def __init__(self):
        self.horiz = 0
        self.depth = 0

    def forward(self, x):
        self.horiz += x

    def up(self, x):
        self.depth -= x

    def down(self, x):
        self.depth += x


def read_input(filename="input.txt"):
    with open(filename, "r") as f:
        data = f.readlines()
    return data


def main(filename="input.txt"):
    directions = read_input(filename)
    sub = Submarine()
    for d in directions:
        verb, distance = d.split()
        if verb == "forward":
            sub.forward(int(distance))
        elif verb == "down":
            sub.down(int(distance))
        elif verb == "up":
            sub.up(int(distance))
        else:
            raise ValueError(f"unknown verb in line {d}")

    return sub.horiz * sub.depth


if __name__ == "__main__":
    result = main()
    print(result)
