# https://codeforces.com/problemset/problem/500/A

def main():
    n, t = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    i = 1
    while True:
        i = a[i-1] + i
        if i == t:
            print("YES")
            return
        elif i > t:
            print("NO")
            return

if __name__ == "__main__":
    main()