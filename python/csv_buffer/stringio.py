import time
import tracemalloc

from contextlib import closing
from csv import DictWriter
from io import StringIO
from os import stat
from sys import getsizeof


BYTE_TO_MEGABYTE = 1024 * 1024


tracemalloc.start()
start_time = time.perf_counter()
with closing(StringIO()) as buffer:
    writer = DictWriter(buffer, fieldnames=['ID'])
    for id in range(10000000):
        writer.writerow({
            'ID': str(id)
        })

    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"Execution time {execution_time}s")

    current, peak = tracemalloc.get_traced_memory()
    s = buffer.getvalue()
    print(f'Memory usage - Current {current / BYTE_TO_MEGABYTE} MB, peak {peak / BYTE_TO_MEGABYTE} MB')
    print(f'String length {len(s)}, memory size {getsizeof(s) / BYTE_TO_MEGABYTE} MB')

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')
print("\nTop 10 memory usage")
for stat in top_stats[:10]:
    print(stat)

tracemalloc.stop()
