import tracemalloc

tracemalloc.start()

for i in range(3):
    temp = [j for j in range(100000)]
    current, peak = tracemalloc.get_traced_memory()
    print(
        f"{i=}: current={current / 1024 / 1024:.2f} МБ, peak={peak / 1024 / 1024:.2f} МБ"
    )
    tracemalloc.reset_peak()  # Сброс пика после каждой итерации
