# https://www.acmicpc.net/problem/1107
import sys
input = sys.stdin.readline 

INF = int(1e9)
n = int(input())

m = int(input())

# broken :  고장난 버튼 저장 
broken = list(map(int,input().split()))

# answer : 현재 위치가 100이므로 최솟값은 +나 -로만 이동한 경우인 abs(100-n)이다. 
answer= abs(100-n)

# 채널 수가 무한대 이므로 1000001 까지 탐색
for i in range(1000001):

  for j in range(len(str(i))):
    # 숫자에 고장난 버튼이 포함되어 있으면 break
    if int(str(i)[j]) in broken: 
      break
    # 마지막까지 고장난 버튼이 없다면 
    elif j == len(str(i)) -1:
      # 현재 위치로 이동하기 위해 누른 버튼 수 + 현재 위치에서 +,-로 n까지 이동하는 거리와 answer 중 최솟값 갱신 
      answer = min(answer, len(str(i)) + abs(i-n))

print(answer)