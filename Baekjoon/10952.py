# A+B - 5
while True:
    a, b = map(int, input().split())
    if not a and not b:
        break
    print(a + b)

# for _ in sys.stdin:
#     a, b = map(int, _.split())
#     if a and b:
#         print(a + b)
