import string
from sys import stdin


def main():
    n = int(input())
    x = 0
    for i in range(n):
        s = str(stdin.readline())
        if "+" in s:
            x += 1
        else:
            x -=1
    print(x)

if __name__ == "__main__":
    main()