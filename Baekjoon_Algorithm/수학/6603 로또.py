# https://www.acmicpc.net/problem/6603
from itertools import combinations 

while True :
  s = list(map(int,input().split()))

  if s[0] == 0:
    break
  else:
    combine = list(combinations(s[1:],6))
    for i in combine :
      print(*i)
    print()