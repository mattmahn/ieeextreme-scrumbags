#!/usr/bin/env python3

from math import floor


def main():
    vals = input().split()
    carbon = int(vals[0])
    hydrogen = int(vals[1])
    oxygen = int(vals[2])

    carbon_diox = 0.25 * (2 * oxygen - hydrogen)
    glucose = (carbon - carbon_diox) / 6
    water = -carbon + carbon_diox + hydrogen / 2

    if water < 0 or carbon_diox < 0 or glucose < 0:
        print('Error')
    else:
        print(floor(water), floor(carbon_diox), floor(glucose))


main()
