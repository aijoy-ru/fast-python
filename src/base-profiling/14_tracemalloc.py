import tracemalloc

tracemalloc.start()
lst = [i for i in range(10000)]
snapshot = tracemalloc.take_snapshot()
tracemalloc.stop()

snapshot.dump("snapshot.out")  # Сохраняем снимок
print("Снимок памяти сохранён в файл.")

snapshot_loaded = tracemalloc.Snapshot.load("snapshot.out")
print("Загруженный снимок:")
for stat in snapshot_loaded.statistics("lineno")[:3]:
    print(stat)
