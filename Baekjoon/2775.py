# 부녀회장이 될테야
a = [list(range(1, 15))]
for _ in range(int(input())):
    k, n = (int(input()) for _ in range(2))
    while k >= len(a):
        b = a[-1].copy()
        for i in range(1, 14):
            b[i] += b[i - 1]
        a.append(b)
    print(a[k][n - 1])
