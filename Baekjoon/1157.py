# 단어 공부
a = input().upper()
a = {c: a.count(c) for c in set(a)}
m = max(a.values())
k = [k for k, v in a.items() if m == v]
print(k[0] if len(k) == 1 else '?')
