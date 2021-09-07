# 한수
def a(n: int) -> bool:
    return n // 10 % 10 * 2 == n // 100 + n % 10


print(sum(1 if i < 100 else a(i) for i in range(1, int(input())+1)))
