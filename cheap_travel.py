# https://codeforces.com/problemset/problem/466/A

def main():
    n, m, a, b = [int(x) for x in input().split()]
    first = n * a
    m_ticket_to_buy = ((n//m) * b)+ (min((n%m)*a, b))
    print(min(first, m_ticket_to_buy))

if __name__ == "__main__":
    main()