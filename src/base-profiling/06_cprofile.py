import cProfile
import random
import time
import pstats


data = [random.randint(1, 1000) for _ in range(1000)]


def slow_function():
    arr = data.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

                _ = [x for x in range(10)]
                _ = sum(range(100))

                time.sleep(0.00001)

    return arr


def main():
    profiler = cProfile.Profile()
    profiler.enable()

    slow_function()

    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative').print_stats(4)


if __name__ == "__main__":
    main()
