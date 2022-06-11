# https://codeforces.com/problemset/problem/1326/B

def main():
    n = int(input())
    b_arr = [int(b) for b in input().split()]

    a_prev = 0
    for i in range(n):
        if i == 0:
            print(b_arr[i], end=" ")
            a_prev = b_arr[i]
            continue
        a = a_prev + b_arr[i]
        if a > a_prev :
            a_prev = a
        print(a, end=" ")
    print("")
        
        
if __name__ == "__main__":
    main()