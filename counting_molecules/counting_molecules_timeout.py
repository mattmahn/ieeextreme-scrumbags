#!/bin/env python


def main():
    process_test_case()


def process_test_case():
    stuff = [int(x) for x in input().split()]

    num_carbon = stuff[0]
    num_hydrogen = stuff[1]
    num_oxygen = stuff[2]

    total = num_carbon + num_hydrogen + num_oxygen

    for num_waters in range(int(total / 3) + 1):
        for num_glucose in range(int(total / 24) + 1):
            for num_carbon_dioxide in range(int(total / 3) + 1):
                if (num_waters + 6*num_glucose + 2*num_carbon_dioxide == num_oxygen) and (2*num_waters + 12*num_glucose == num_hydrogen) and (6*num_glucose + num_carbon_dioxide == num_carbon):
                    print(num_waters, num_carbon, num_glucose)
                    return

    print('Error')


main()
