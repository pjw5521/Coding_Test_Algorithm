# 문제 https://www.acmicpc.net/problem/10816
import sys

r =  sys.stdin.readline

n = int(r())
data = list(map(int,r().split()))
# 정렬 꼭 해줘야함. 이진탐색은 정렬 가정 
data.sort()
data_dic={}

for i in data:
  if i not in data_dic:
    data_dic[i] = 1
  else:
    data_dic[i] += 1

m = int(r())
search = list(map(int,r().split()))

for i in search:
  start = 0 
  end = n - 1

  while start <= end :
    mid = (start + end) //2 
    if data[mid] == i:
      break
    if data[mid] < i:
      start = mid + 1
    else :
      end = mid - 1 
  
  if data[mid] == i:
    print(data_dic[i], end = " ")
  else:
    print(0, end =" ")