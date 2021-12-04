#! /usr/bin/env python3

from collections import defaultdict

def read_input(filename="input.txt"):
    with open(filename, "r") as f:
        data = f.readlines()
    return data


def count_bits(bitstrings):
    """
    Count the frequency of each bit in the bitstrings array.
    Return an array where each element represents a bit position,
    and holds a dict that contains bit counts for that bit position.
    :param bitstrings: list(str)
    :return: dict
    """
    bitcount = [defaultdict(int) for _ in range(0, len(bitstrings[0]))]
    for s in bitstrings:
        for i, c in enumerate(s):
            bitcount[i][c] += 1
    return bitcount


def gamma(bitcount):
    """
    Determine the gamma rate derived from the given bitcount.
    The gamma rate is calculated by generating a string of binary
    digits in which each bit is the most common bit for that bit
    position.
    :param bitcount: list(dict)
    :return: int
    """
    gamma_str = ""
    for count in bitcount:
        gamma_str += max(count.keys(), key=lambda x: count[x])
    return int(gamma_str, base=2)


def epsilon(bitcount):
    """
    Determine the epsilon rate derived from the given bitcount.
    The epsilon rate is calculated by generating a string of binary
    digits in which each bit is the least common bit for that bit
    position.

    :param bitcount: list(dict)
    :return: int
    """
    epsilon_str = ""
    for count in bitcount:
        epsilon_str += min(count.keys(), key=lambda x: count[x])
    return int(epsilon_str, base=2)


def main(filename="input.txt"):
    data = read_input(filename)
    bitcount = count_bits(data)
    power_consumption = gamma(bitcount) * epsilon(bitcount)
    return power_consumption


if __name__ == "__main__":
    result = main("input.txt")
    print(result)
