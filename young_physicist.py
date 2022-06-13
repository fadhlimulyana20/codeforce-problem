# https://codeforces.com/problemset/problem/69/A
# WA on test 81

def solve(n: int):
    x, y, z = 0, 0, 0
    for i in range(n):
        xi, yi, zi = [int(num) for num in input().split()]
        x += xi
        y += yi
        z += zi
    return x + y + z == 0


def main():
    n = int(input())
    if solve(n):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()