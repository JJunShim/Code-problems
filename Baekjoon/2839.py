# 설탕 배달
n = int(input())
q, r = [0] * 2
for i in range(n // 5, -1, -1):
    q, r = divmod(n - 5 * i, 3)
    if not r:
        q += i
        break
print(-1 if r else q)
