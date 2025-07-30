import random


def bubble_sort():
    arr = [random.randint(1, 1000) for _ in range(1000)]
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def main():
    bubble_sort()


if __name__ == "__main__":
    main()
