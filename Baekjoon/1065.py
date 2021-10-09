# 한수
def f(x):
    q, r = divmod(x, 10)
    return q // 10 + r == q % 10 * 2


n = int(input())
print(n if n < 100 else sum(map(f, range(100, n + 1))) + 99)
