# 문제 360쪽
# https://www.acmicpc.net/problem/18310
# 중간값이 가장 최솟값이 됨 
import sys

input =  sys.stdin.readline

n = int(input())

data = list(map(int,input().split()))
data.sort()

print(data[ (n-1) // 2 ])