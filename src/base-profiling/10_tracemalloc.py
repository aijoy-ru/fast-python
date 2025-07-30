import tracemalloc

tracemalloc.start()

lst = [i for i in range(10**6)]

current, peak = tracemalloc.get_traced_memory()
print(f"Текущее использование памяти: {current / 1024 / 1024:.2f} МБ")
print(f"Пиковое использование памяти: {peak / 1024 / 1024:.2f} МБ")

tracemalloc.stop()
