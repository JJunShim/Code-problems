# 베르트랑 공준
import sys
a = [int(l) for l in sys.stdin][:-1]
n = max(a) * 2
sieve = [True] * n
for i in range(2, int(n ** .5) + 1):
    if sieve[i - 1]:
        for j in range(i * 2, n + 1, i):
            sieve[j - 1] = False
print(*(sum(sieve[m: m * 2]) for m in a))
