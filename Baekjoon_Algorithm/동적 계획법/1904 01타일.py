# https://www.acmicpc.net/problem/1904
'''
d[n] = d[n-1] + d[n-2]
'''
import sys
input = sys.stdin.readline
count = [ 1, 2 ]
n = int(input())

for i in range(2,n):
# 배열에 대입할 때 나누기 연산 안하고 출력할 때 해주면 메모리 초과 
  count.append((count[i-1]+ count[i-2]) % 15746)

print(count.pop())