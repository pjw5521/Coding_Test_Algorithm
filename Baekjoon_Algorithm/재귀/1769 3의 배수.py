# https://www.acmicpc.net/problem/1769
def sol(n,cnt):
  if len(n) == 1 :
    print(cnt)
    if int(n) % 3 == 0 :
      print("YES")
    else:
      print("NO")
    return 
  s = 0
  # 자릿수 합
  for i in n:
    s += int(i)
  sol(str(s),cnt+1)
  
n = input()
sol(n,0)