#!/usr/bin/env python3

import math


def prime_factors(N):
    pf = []
    if N % 2 == 0:
        pf.append(2)
        while N % 2 == 0:
            N = N >> 1
    for x in range(3, math.floor(math.sqrt(N)), 2):
        if N % x == 0:
            pf.append(x)
            while N % x == 0:
                N = int(N / x)
    if N > 2:
        pf.append(N)
    return pf


print(prime_factors(10**12 - 139))
