#!/bin/env python


def main():
    for _ in range(100):
        find_last(_)


def find_last(_):
    petals = list(range(_ + 1))[1:]
    print('N:', _)
    index = 0
    he_loves_me = True
    while len(petals) > 1:
        if he_loves_me:
            index = (index + 1) % len(petals)
            he_loves_me = False
        else:
            del petals[index]
            he_loves_me = True
    [print('\tlast:', x) for x in petals]


main()
