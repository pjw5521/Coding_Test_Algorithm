# https://www.acmicpc.net/problem/15829
n = int(input())

s = input()
result = 0

for i in range(n):
  # a의 아스키코드 값이 97이므로 
  num = ord(s[i]) % 96
  result += num * 31**(i)

print(result% 1234567891)