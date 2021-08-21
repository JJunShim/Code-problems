# 곱셈
a = int(input())
b = map(int, list(reversed(input())))
result = 0

for i, n in enumerate(b):
    n *= a
    result += n * 10 ** i
    print(n)
print(result)
