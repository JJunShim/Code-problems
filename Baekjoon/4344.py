# 평균은 넘겠지
for _ in range(int(input())):
    n, *a = [int(_) for _ in input().split()]
    m = sum(a) / n
    print(f'{len([_ for _ in a if _ > m]) / n * 100:.3f}%')
