# https://www.acmicpc.net/problem/9935
s = list(map(str,input()))

expo = list(map(str,input()))
stack = []

for i in range(len(s)):
  stack.append(s[i])
  # 스택의 마지막 문자와 폭발 문자열의 마지막 문자가 같고, 스택의 길이가 폭발 문자열의 길이보다 길다면 
  if stack[-1] == expo[-1] and len(stack) >= len(expo):
    # 스택에 폭발 문자열 있는지 확인 
    if stack[-len(expo):] == expo:
      # 폭발 문자열이 있다면 폭발 문자열의 길이만큼 스택에서 문자 제거 
      for _ in range(len(expo)):
        stack.pop()
        
if stack :
  print("".join(stack))
else:
  print("FRULA")