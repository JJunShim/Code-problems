# 시험 성적
a = int(input())
result = ['A', 'B', 'C', 'D', 'F']
if a >= 90:
    print(result[0])
elif a >= 80:
    print(result[1])
elif a >= 70:
    print(result[2])
elif a >= 60:
    print(result[3])
else:
    print(result[4])
