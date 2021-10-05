# 팩토리얼
def f(x):
    return 1 if x <= 1 else x * f(x - 1)


print(f(int(input())))
