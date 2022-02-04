# https://www.acmicpc.net/problem/4949
stack = []

while True:
  s = input()
  result = True
  stack = []

  if s == '.':
    break

  for i in s:
    # stack에 추가 
    if i == '(' or i =='[':
      stack.append(i)
      
    # stack이 비어있지 않고 쌍이 맞으면 pop 틀리면 no 출력 
    elif i == ']':
      if len(stack) > 0 and stack[-1] == '[':
        stack.pop()
      else :
        print('no')
        result = False
        break
        
    # stack이 비어있지 않고 쌍이 맞으면 pop 틀리면 no 출력 
    elif i == ')':
      if len(stack) > 0 and stack[-1] == '(':
        stack.pop()
      else :
        print('no')
        result = False
        break
  
  if result :
    # 스택에 괄호가 남아있으면 No 
    if stack:
      print('no')
    else:
      print('yes')  