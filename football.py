# If there are at least 7 players of some team standing one after another,

def main():
    arr = [int(i) for i in list(input())]
    consecutive = 0
    arr_prev = None
    for i in range(len(arr)):
        if i == 0:
            arr_prev = arr[i]
            consecutive = 1
            continue
        if arr[i] == arr_prev:
            consecutive += 1
        else:
            consecutive = 1
        arr_prev = arr[i]
        if consecutive >= 7:
            print("YES")
            return
    print("NO")

if __name__ == "__main__":
    main()