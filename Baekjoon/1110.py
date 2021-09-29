# 더하기 사이클
n = m = int(input())
i = 0
while True:
    i += 1
    q, r = divmod(m, 10)
    m = (r * 10) + ((q + r) % 10)
    if m == n:
        break
print(i)
