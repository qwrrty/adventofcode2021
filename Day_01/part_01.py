#! /usr/bin/env python

def read_input(filename="input.txt"):
    with open(filename, "r") as f:
        data = [int(x) for x in f.readlines()]
    return data


def main():
    previous_depth = None
    increases = 0
    for depth in read_input():
        if previous_depth is not None:
            if depth > previous_depth:
                increases += 1
        previous_depth = depth
    return increases


if __name__ == "__main__":
    result = main()
    print(result)
