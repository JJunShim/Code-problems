# 소수 구하기
m, n = map(int, input().split())
sieve = [True] * n
for i in range(2, int(n ** .5) + 1):
    if sieve[i - 1]:
        for j in range(i * 2, n + 1, i):
            sieve[j - 1] = False
for i in range(m if m > 1 else 2, n + 1):
    if sieve[i - 1]:
        print(i)
