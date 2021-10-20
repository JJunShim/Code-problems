# 직사각형에서 탈출
x, y, w, h = (int(s) for s in input().split())
print(min(x, y, w - x, h - y))
