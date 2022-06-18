# https://codeforces.com/problemset/problem/492/B
import sys

def swap(arr: list, i: int, j: int):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def partition(arr: list, low: int, high: int) -> int:
    pivot = arr[low]
    i, j = low, high
    
    while (i<j):
        while (arr[i] <= pivot):
            i += 1
        while (arr[j] > pivot):
            j -= 1
        if (i < j):
            swap(arr, i, j)
    swap(arr, low, j)
    return j

def quick_sort(arr: list, low: int, high: int) :
    if (low < high):
        j = partition(arr, low, high)
        print(arr)
        quick_sort(arr, low, j)
        quick_sort(arr, j+1, high)

if __name__ == "__main__":
    n, l = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    quick_sort(arr, 0, len(arr)-1)
    maxsize = 0

