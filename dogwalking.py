#!/bin/env python


def main():
    test_cases = input()
    for _ in range(int(test_cases)):
        process_test_case()


def calculate_ranges(dog_sizes):
    return [dog_sizes[i] - dog_sizes[i - 1] for i, _ in enumerate(dog_sizes[1:], 1)]


def process_test_case():
    dog_sizes = []

    num_dogs, num_walkers = [int(q) for q in input().split(' ')]
    for x in range(num_dogs):
        dog_sizes.append(int(input()))
        # print(dog_sizes)

    dog_sizes.sort()
    ranges = calculate_ranges(dog_sizes)
    ranges.sort()

    print(sum(ranges[:(num_dogs - num_walkers)]))


main()
