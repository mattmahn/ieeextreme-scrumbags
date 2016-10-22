#!/bin/env python


def main():
    test_cases = int(input())

    for _ in range(test_cases):
        process_test_case()


def process_test_case():
    games = int(input())

    total = 0

    for game in range(games):
        num_piles = int(input())
        for x in input().split():
            total += (int(x) - 1)/2

    if total % 2 == 0:
        # second player wins
        print('Bob')
    else:
        # first player wins
        print('Alice')


main()
