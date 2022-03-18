# https://www.acmicpc.net/problem/1918
s = list(input())
stack = []
ans = ""
for i in s:
    if i.isalpha():
        ans += i 
    else :
        if i == '(':
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()
        elif i == '*' or i =='/':
            while stack and (stack[-1] =='*' or stack[-1] =='/' ):
                ans += stack.pop()
            stack.append(i)
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.append(i)
            
while stack:
    ans += stack.pop()
print(ans)