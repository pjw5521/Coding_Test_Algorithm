# https://www.acmicpc.net/problem/11286﻿
import heapq 
import sys 
input = sys.stdin.readline 

n = int(input())

heap = []

for _ in range(n):
  num = int(input())

  if num != 0:
    heapq.heappush(heap, (abs(num), num))
  else:
    if heap:
      print(heapq.heappop(heap)[1])
    else:
      print(0)