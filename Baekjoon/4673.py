# 셀프 넘버
def f(x):
    q = x + 1
    while q:
        q, r = divmod(q, 10)
        x += r
    return x


l = 10000
a = [True] * l
for i in range(l):
    try:
        a[f(i)] = False
    except:
        continue
for i, _ in enumerate(a, 1):
    if _:
        print(i)
