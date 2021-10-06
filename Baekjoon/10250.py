# ACM 호텔
for _ in range(int(input())):
    h, _, n = (int(s) for s in input().split())
    f = n % h
    print((f if f else h) * 100 + (n - 1) // h + 1)
