# 윤년
a = int(input())
print(1 if not a % 4 and (a % 100 or not a % 400) else 0)
