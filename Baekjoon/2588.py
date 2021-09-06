# 곱셈
a = int(input())
b = input()
print(*(a * int(n) for n in b[::-1]), a * int(b))
