def main():
    m, n = [int(x) for x in input().split()]
    area = m*n
    cards = area//2
    print(cards)

if __name__ == "__main__":
    main()