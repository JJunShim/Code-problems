# 셀프 넘버
def solve(num: int) -> int:
    result = num
    while num:
        num, s = divmod(num, 10)
        result += s
    return result


a = list(range(10000))
for i in range(10000):
    try:
        a[solve(i)] = None
    except:
        pass
print(*(_ for _ in a if _))
