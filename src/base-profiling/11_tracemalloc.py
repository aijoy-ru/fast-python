import tracemalloc

tracemalloc.start()

snapshot1 = tracemalloc.take_snapshot()

data = [str(i) * 100 for i in range(100000)]

snapshot2 = tracemalloc.take_snapshot()

# Сравнить снимки, чтобы найти самые дорогие строки
top_stats = snapshot2.compare_to(snapshot1, "lineno")

print("ТОП строк по потреблению памяти:")
for stat in top_stats[:5]:
    print(stat)

tracemalloc.stop()
