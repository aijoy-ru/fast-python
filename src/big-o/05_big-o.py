def bubble_sort(arr):
    n = len(arr)
    for i in range(n):  # n итераций
        for j in range(0, n - i - 1):  # До n итераций
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
