import math
import os
import sys
from bisect import bisect_left, bisect_right
from io import BytesIO, IOBase

def solve():
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    num_pos = [0] * (n + 1)
    for i, num in enumerate(array):
        num_pos[num] = i

    count = 0
    for ind, num in enumerate(array):
        if num == 1 or num_pos[num - 1] > ind:
            count += 1

    result = []
    for _ in range(m):
        x, y = map(int, input().split())
        if x > y:
            x, y = y, x
        x -= 1
        y -= 1
        if array[x] + 1 == array[y]:
            count += 1
        elif array[x] == array[y] + 1:
            count -= 1
        if array[x] - 1 > 0 and x < num_pos[array[x] - 1] < y:
            count -= 1
        if array[x] + 1 <= n and x < num_pos[array[x] + 1] < y:
            count += 1
        if array[y] - 1 > 0 and x < num_pos[array[y] - 1] < y:
            count += 1
        if array[y] + 1 <= n and x < num_pos[array[y] + 1] < y:
            count -= 1

        array[x], array[y] = array[y], array[x]
        num_pos[array[x]] = x
        num_pos[array[y]] = y
        result.append(str(count))
    return '\n'.join(result)



def main():
    print(solve())

# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()