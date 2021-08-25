# X보다 작은 수
_, x = map(int, input().split())
print(*[_ for _ in input().split() if int(_) < x])
