#!/usr/bin/env python3

def make_base_symbols(symbols):
    """ :param: symbols {String} """
    base_symbols = dict()
    number = 0
    for c in symbols:
        base_symbols[c] = number
        number += 1
    return base_symbols

def main():
    stuff_raw = input()
    stuff = stuff_raw.split(' ')

    base = int(stuff[0])
    base_chars = stuff[1]

    num_1_raw = input()
    num_2_raw = input()

    num_1 = num_1_raw.strip()
    num_2 = num_2_raw[1:].strip()

    dashes = input()
    questions = input()

    base_symbols = make_base_symbols(base_chars)

    num_1_based10 = from_base(num_1, base, base_symbols)
    num_2_based10 = from_base(num_2, base, base_symbols)

    sum = num_1_based10 + num_2_based10

    print(stuff_raw)
    print(num_1_raw)
    print(num_2_raw)
    print(dashes)
    print(" " + int2base(sum, base, base_chars))


def from_base(num_str, base, base_symbols):
    num = [base_symbols[x] for x in num_str]
    num_str_rev = num[::-1]

    result = 0

    for i in range(len(num_str)):
        result += (base ** i) * num_str_rev[i]

    return result


def int2base(x,b,alphabet='0123456789abcdefghijklmnopqrstuvwxyz'):
    if x<=0:
        if x==0:
            return alphabet[0]
        else:
            return  '-' + int2base(-x,b,alphabet)
    # else x is non-negative real
    rets=''
    while x>0:
        x,idx = divmod(x,b)
        rets = alphabet[idx] + rets
    return rets


main()