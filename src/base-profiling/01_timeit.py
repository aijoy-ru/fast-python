import timeit


result = timeit.timeit("sum(range(1000))", number=10000)
print(result)
