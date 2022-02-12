# https://www.acmicpc.net/problem/9012
test = int(input())

for _ in range(test):
  s = input()
  result = 0

  for i in s:
    if i == '(':
      result += 1 
    else :
      result -= 1
    # 짝을 이루지 않는 ) 가 들어왔다는 뜻 
    if result < 0 :
      print('NO')
      break 
    
  # ( 괄호가 남아있다는 뜻 
  if result > 0 :
    print('NO')
  # 짝이 맞으면 
  elif result == 0 :
    print('YES')
