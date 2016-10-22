#!/usr/bin/env python3

import math


def prime_factors(n, b):
    pf = []

    if n % 2 == 0:
        pf.append(2)
        while n % 2 == 0:
            n >>= 1

    for x in range(3, math.floor(math.sqrt(b)), 2):
        if n % x == 0:
            pf.append(x)
            while n % x == 0:
                n = int(n / x)

    if n > 2:
        pf.append(n)

    return pf


def is_divisible(num, factors):
    for x in factors:
        if num % x == 0:
            return True

    return False


def main():
    cases = int(input())

    for _ in range(cases):
        string = input().split(' ')

        N = int(string[0])
        A = int(string[1])
        B = int(string[2])

        primes = prime_factors(N, B)

        summation = 0

        for x in range(A, B + 1):
            if not is_divisible(x, primes):
                summation += x

        print(summation % 1000000007)


main()
