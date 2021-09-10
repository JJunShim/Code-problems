# 그룹 단어 체커
def a(s: str):
    if list(s) == sorted(s, key=s.find):
        return True
    return False


print(sum(a(input()) for _ in range(int(input()))))
