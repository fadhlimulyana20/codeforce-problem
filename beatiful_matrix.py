def main():
    m = []
    x, y = 0, 0
    for i in range(5):
        arr = [int(x) for x in input().split()]
        j = None
        try:
            j = arr.index(1)
        except ValueError:
            pass
        if j != None:
            x, y = i, j
    x_distance = abs(x-2)
    y_distance = abs(y-2)
    print(x_distance + y_distance)


if __name__ == "__main__":
    main()