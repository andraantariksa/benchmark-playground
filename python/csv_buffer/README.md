# `StringIO` vs `tempfile` Benchmark for CSV Buffer

## Benchmark

### `StringIO`

```
Execution time 69.10216833300001s
Memory usage - Current 84.90448093414307 MB, peak 91.19870853424072 MB
String length 88888890, memory size 84.77109813690186 MB

Top 10 memory usage
/home/andra/Projects/benchmark-playground/python/csv_buffer/stringio.py:28: size=84.8 MiB, count=1, average=84.8 MiB
/usr/lib/python3.10/csv.py:154: size=128 KiB, count=2, average=64.2 KiB
/home/andra/Projects/benchmark-playground/python/csv_buffer/stringio.py:23: size=1136 B, count=2, average=568 B
/home/andra/Projects/benchmark-playground/python/csv_buffer/stringio.py:16: size=552 B, count=3, average=184 B
/usr/lib/python3.10/csv.py:151: size=495 B, count=3, average=165 B
/home/andra/Projects/benchmark-playground/python/csv_buffer/stringio.py:32: size=416 B, count=1, average=416 B
/home/andra/Projects/benchmark-playground/python/csv_buffer/stringio.py:17: size=224 B, count=3, average=75 B
/usr/lib/python3.10/csv.py:145: size=167 B, count=2, average=84 B
/usr/lib/python3.10/csv.py:139: size=160 B, count=2, average=80 B
/home/andra/Projects/benchmark-playground/python/csv_buffer/stringio.py:27: size=56 B, count=2, average=28 B
```

### `tempfile`

```
Execution time 60.60653837399968s
Memory usage - Current 0.15497970581054688 MB, peak 0.24612903594970703 MB
File size 84.77003002166748 MB

Top 10 memory usage
/usr/lib/python3.10/csv.py:154: size=129 KiB, count=4, average=32.2 KiB
/usr/lib/python3.10/tempfile.py:285: size=2592 B, count=2, average=1296 B
/home/andra/Projects/benchmark-playground/python/csv_buffer/file.py:26: size=1792 B, count=18, average=100 B
/usr/lib/python3.10/tempfile.py:698: size=1781 B, count=16, average=111 B
/home/andra/Projects/benchmark-playground/python/csv_buffer/file.py:14: size=1448 B, count=3, average=483 B
/usr/lib/python3.10/tempfile.py:293: size=976 B, count=2, average=488 B
/usr/lib/python3.10/tempfile.py:438: size=872 B, count=2, average=436 B
/home/andra/Projects/benchmark-playground/python/csv_buffer/file.py:15: size=696 B, count=4, average=174 B
/usr/lib/python3.10/csv.py:139: size=584 B, count=3, average=195 B
/usr/lib/python3.10/tempfile.py:695: size=528 B, count=1, average=528 B
```

## Conclusion

`tempfile` wins in term of memory usage and time compared with `StringIO`.

See https://stackoverflow.com/questions/25580925/why-is-stringio-object-slower-than-real-file-object
