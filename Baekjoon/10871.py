# X보다 작은 수
x = int(input().split()[1])
print(*(_ for _ in input().split() if int(_) < x))
