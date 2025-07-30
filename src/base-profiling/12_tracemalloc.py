import tracemalloc

tracemalloc.start()

l1 = [i for i in range(10000)]
l2 = [i * i for i in range(10000)]
l3 = [i * i * i for i in range(10000)]

snapshot = tracemalloc.take_snapshot()
stats = snapshot.statistics("lineno")

print("Это список мест с максимальным выделением памяти:")
for stat in stats[:3]:
    print(stat)
