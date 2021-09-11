# 알파벳 찾기
import string
a = input()
for c in string.ascii_lowercase:
    try:
        print(a.index(c))
    except:
        print(-1)
