# 소수 찾기
def f(x):
    if x < 2:
        return False
    for i in range(2, int(x ** .5) + 1):
        if not x % i:
            return False
    return True


input()
print(sum(f(int(x)) for x in input().split()))
