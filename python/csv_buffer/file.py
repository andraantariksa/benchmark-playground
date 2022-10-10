import time
import tracemalloc

from csv import DictWriter
from os import stat
from tempfile import NamedTemporaryFile


BYTE_TO_MEGABYTE = 1024 * 1024


tracemalloc.start()
start_time = time.perf_counter()
with NamedTemporaryFile(mode='w+') as buffer:
    writer = DictWriter(buffer, fieldnames=['ID'])
    for id in range(10000000):
        writer.writerow({
            'ID': str(id)
        })

    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"Execution time {execution_time}s")

    file_stats = stat(buffer.name)
    current, peak = tracemalloc.get_traced_memory()
    print(f'Memory usage - Current {current / BYTE_TO_MEGABYTE} MB, peak {peak / BYTE_TO_MEGABYTE} MB')
    print(f'File size {file_stats.st_size / BYTE_TO_MEGABYTE} MB')

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')
print("\nTop 10 memory usage")
for stat in top_stats[:10]:
    print(stat)

tracemalloc.stop()
