# 사분면 고르기
a, b = (int(input()) for _ in range(2))
if a > 0 and b > 0:
    print(1)
elif a < 0 and b > 0:
    print(2)
elif a < 0 and b < 0:
    print(3)
elif a > 0 and b < 0:
    print(4)