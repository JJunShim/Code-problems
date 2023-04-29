for _ in range(int(input())):
    x, y = map(int, input().split())
    n, q = [y - x] * 2
    r = 2
    while q > 2 and r:
        q -= r
        q, r = divmod(q, 2)
        n -= q
    print(n)
