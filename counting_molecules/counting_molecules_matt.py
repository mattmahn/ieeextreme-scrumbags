#!/usr/bin/env python3

def main():
    vals = input().split()
    carbon = int(vals[0])
    hydrogen = int(vals[1])
    oxygen = int(vals[2])

    carbon_diox = carbon - oxygen
    glucose = (carbon - carbon_diox) / 6
    water = -carbon + carbon_diox + hydrogen / 2

    print(water, carbon_diox, glucose)


main()
