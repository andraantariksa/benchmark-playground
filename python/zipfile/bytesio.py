from contextlib import closing
from io import BytesIO
import sys
from tempfile import NamedTemporaryFile
import timeit
from zipfile import ZipFile
from memory_profiler import profile

zen = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""


def bench():
    with closing(BytesIO()) as buffer:
        with ZipFile(buffer, 'w') as zipfile:
            for i in range(10000):
                zipfile.writestr(f'zen-{i}.txt', zen)

        buffer.seek(0)
        with NamedTemporaryFile('wb+') as zipfile:
            zipfile.write(buffer.getvalue())

if __name__ == '__main__':
    if sys.argv[-1] == 'time':
        print(timeit.timeit("bench()", globals=locals(), number=10))
    else:
        profile(bench())
