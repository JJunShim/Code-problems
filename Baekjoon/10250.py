# ACM 호텔
from sys import stdin


def room(h, n):
    a, b = divmod(n, h)
    if not b:
        a -= 1
        b = h
    return b * 100 + a + 1


def room(h, n):
    f = n % h
    return (f if f else h) * 100 + (n - 1) // h + 1


_ = input()
for l in stdin:
    h, _, n = map(int, l.split())
    print(room(h, n))
