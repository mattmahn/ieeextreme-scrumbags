#!/usr/bin/env python3

chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
         'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
         'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
         'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
char_map = dict()
for i, c in enumerate(chars):
    char_map[c] = i


def make_base_symbols(symbols):
    """ :param: symbols {String} """
    base_symbols = dict()
    number = 0
    for c in symbols:
        base_symbols[c] = number
        number += 1
    return base_symbols
