def main():
    for _ in range(int(input())):
        num = int(input())

        last_roll = 2 ** (num.bit_length() - 1)

        n = (num - (last_roll - 1)) * 2 - 1

        print(n)

main()