# Классический пример: перебор всех троек элементов массива для поиска суммы,
# равной заданному числу.
def has_triplet_sum(arr, S):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == S:
                    return True
    return False
