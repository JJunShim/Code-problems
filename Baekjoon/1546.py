# 평균
n = int(input())
s = m = 0
for x in input().split():
    x = int(x)
    if x > m:
        m = x
    s += x
print(100 * s / m / n)
