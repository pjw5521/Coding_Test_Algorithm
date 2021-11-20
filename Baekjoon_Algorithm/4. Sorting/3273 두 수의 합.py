#https://www.acmicpc.net/problem/3273

# 조합 라이브러리 사용해서 풀거나, 반복문 사용하면 메모리 초과
'''
import sys
input = sys.stdin.readline
import itertools 

n = int(input())
 
data = list(map(int,input().split()))

x = int(input())

result = list(itertools.combinations(data,2))

count = 0 
for a, b in result:
  if a+b == x:
    count += 1 

print(count)
'''

# 투 포인터 사용
import sys
input = sys.stdin.readline 

n = int(input())
 
data = list(map(int,input().split()))

x = int(input())

data.sort()

count = 0
left = 0
right = n-1

while left != right:
  if data[left]+ data[right] == x:
    count +=1
    left += 1
  elif data[left] + data[right] > x:
    right -= 1
  else:
    left+=1

print(count)