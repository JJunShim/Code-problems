# OX퀴즈
from sys import stdin
_ = input()
print(*(sum((sum(range(1, len(i)+1)) for i in l.strip().split(sep='X')))
      for l in stdin))
