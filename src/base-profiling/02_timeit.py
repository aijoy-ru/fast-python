import timeit


def sum_for():
    total = 0
    for i in range(1000):
        total += i
    return total


def sum_builtin():
    return sum(range(1000))


print("for-loop:", timeit.timeit(sum_for, number=10000))
print("builtin sum:", timeit.timeit(sum_builtin, number=10000))
