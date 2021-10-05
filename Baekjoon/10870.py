# 피보나치 수 5
def f(x):
    return x if x <= 1 else f(x - 2) + f(x - 1)


print(f(int(input())))
