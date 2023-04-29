def f(x):
    for i in range(2, int(x ** .5) + 1):
        if not x % i:
            return False
    return True


p = [x for x in range(int(input()), int(input()) + 1) if x >= 2 and f(x)]
print(*[sum(p), min(p)] if p else [-1])
