#! /usr/bin/env python

def read_input(filename="input.txt"):
    with open(filename, "r") as f:
        data = [int(x) for x in f.readlines()]
    return data


def window_sum(data, index, size=3):
    return sum([data[i] for i in range(index-size, index)])


def main(filename="input.txt"):
    data = read_input(filename)
    increases = 0
    for x in range(4, len(data)+1):
        if window_sum(data, x) > window_sum(data, x-1):
            increases += 1

    return increases


if __name__ == "__main__":
    result = main()
    print(result)
