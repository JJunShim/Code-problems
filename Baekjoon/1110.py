# 더하기 사이클
n = m = int(input())
i = 0
while True:
    q, r = divmod(m, 10)
    m = r * 10 + (q + r) % 10
    i += 1
    if m == n:
        break
print(i)
