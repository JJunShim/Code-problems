# 한수
def a(n: int) -> bool:
    return n // 10 % 10 * 2 == n // 100 + n % 10


n = int(input())
print(n if n < 100 else 99 + sum(a(i) for i in range(100, n + 1)))
