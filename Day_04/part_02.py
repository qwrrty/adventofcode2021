#! /usr/bin/env python3

import bingo


def read_input(filename="input.txt"):
    with open(filename, "r") as f:
        data = f.readlines()
    return data


def main():
    data = read_input("input.txt")
    result = bingo.play_bingo(data, wins=100)
    print(result)


if __name__ == "__main__":
    main()
