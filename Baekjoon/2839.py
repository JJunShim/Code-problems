# 설탕 배달
n = int(input())
q, r = divmod(n, 5)
for i in range(q, -1, -1):
    q, r = divmod(n - i * 5, 3)
    if not r:
        q += i
        break
print(-1 if r else q)
