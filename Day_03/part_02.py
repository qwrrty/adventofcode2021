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
    bitcount = [defaultdict(int) for _ in bitstrings[0]]
    for s in bitstrings:
        for i, c in enumerate(s):
            bitcount[i][c] += 1
    return bitcount


def filter_bitstrings(bitstrings, bit_criteria):
    """
    Filter a set of bitstrings to a single candidate based on the specified
    bit criteria.

    The solution string is found by repeatedly refining bitstring candidates
    based on whether they fit the bit criteria. First we limit the search
    to candidates whose bit #0 satisfies the specified criteria. Then we
    limit to candidates whose bit #1 satisfies the criteria. The process is
    repeated until only a single candidate remains.

    :param bitstrings: list(str)
    :param bit_criteria: lambda
    :return: int
    """
    candidates = bitstrings.copy()
    for i in range(0, len(bitstrings[0])):
        if len(candidates) == 1:
            break
        # Narrow down the candidate set to strings which satisfy the bit
        # criteria for bit position i
        bitcount = count_bits(candidates)
        target = bit_criteria(bitcount[i])
        candidates = [s for s in candidates if s[i] == target]

    if len(candidates) > 1:
        raise ValueError(f"more than one candidate is left: {candidates}")

    return int(candidates[0], base=2)


def oxygen_generator_criteria(frequency_dict):
    if frequency_dict['0'] > frequency_dict['1']:
        return '0'
    else:
        return '1'


def co2_scrubber_criteria(frequency_dict):
    if frequency_dict['0'] > frequency_dict['1']:
        return '1'
    else:
        return '0'


def main(filename="input.txt"):
    bitstrings = read_input(filename)
    o2_rating = filter_bitstrings(bitstrings, bit_criteria=oxygen_generator_criteria)
    co2_rating = filter_bitstrings(bitstrings, bit_criteria=co2_scrubber_criteria)
    life_support_rating = o2_rating * co2_rating
    return life_support_rating


if __name__ == "__main__":
    result = main()
    print(result)
