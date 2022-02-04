#https://www.acmicpc.net/problem/3986
test = int(input())
cnt = 0 

for _ in range(test):
 s  = input()
 stack = []
   
 for i in s:
  # 스택에서 나올 원소와 같다면 
  if stack and stack[-1] == i:
      stack.pop()
  else :
      stack.append(i)
      
 if not stack:
    cnt += 1 

print(cnt)