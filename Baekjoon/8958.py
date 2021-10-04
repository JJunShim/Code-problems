# OX퀴즈
for _ in range(int(input())):
    l = input().split(sep='X')
    print(sum(sum(range(1, len(s) + 1)) for s in l))
