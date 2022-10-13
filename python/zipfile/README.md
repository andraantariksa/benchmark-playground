# `BytesIO` vs `tempfile` Benchmark for ZIP Buffer

## Benchmark

### `tempfile`

```
Filename: zipfile/file.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    29     20.2 MiB     20.2 MiB           1   @profile
    30                                         def bench():
    31     20.2 MiB      0.0 MiB           1       with NamedTemporaryFile('wb+') as buffer:
    32     20.2 MiB      0.0 MiB           1           with ZipFile(buffer, 'w') as zipfile:
    33     25.6 MiB      0.0 MiB       10001               for i in range(10000):
    34     25.6 MiB      5.4 MiB       10000                   zipfile.writestr(f'zen-{i}.txt', zen)
```

Runtime 6.0171038749995205s

## `BytesIO`

```
Filename: zipfile/bytesio.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    29     20.3 MiB     20.3 MiB           1   @profile
    30                                         def bench():
    31     20.3 MiB      0.0 MiB           1       with closing(BytesIO()) as buffer:
    32     20.3 MiB      0.0 MiB           1           with ZipFile(buffer, 'w') as zipfile:
    33     34.8 MiB      0.5 MiB       10001               for i in range(10000):
    34     34.3 MiB     13.9 MiB       10000                   zipfile.writestr(f'zen-{i}.txt', zen)
    35
    36     34.8 MiB      0.0 MiB           1           buffer.seek(0)
    37     31.8 MiB     -3.0 MiB           1           with NamedTemporaryFile('wb+') as zipfile:
    38     22.6 MiB     -9.1 MiB           1               zipfile.write(buffer.getvalue())
```

Runtime 3.8502429029995255s

## Conclusion

`BytesIO` wins in term of performance and `tempfile` wins in term of memory usage
