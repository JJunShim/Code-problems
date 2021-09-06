# 별 찍기 - 2
n = int(input())
print(*(' ' * (n - i) + '*' * i for i in range(1, n + 1)), sep='\n')
