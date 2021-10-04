# 평균은 넘겠지
for _ in range(int(input())):
    n, *a = (int(x) for x in input().split())
    m = sum(a) / n
    m = sum(x > m for x in a) / n
    print(f'{m * 100:.3f}%')
