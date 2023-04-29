def f(n):
    m = n
    a = []
    i = 2
    while m and i < n:
        q, r = divmod(m, i)
        if r:
            i += 1
            continue
        m = q
        a.append(i)
    return a if a else [n]


n = int(input())
if n > 1:
    print(*f(n))
