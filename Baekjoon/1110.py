# 더하기 사이클
n = m = int(input())
i = 0

while True:
    m = m % 10 * 10 + sum(divmod(m, 10)) % 10
    i += 1
    if m == n:
        break

print(i)
