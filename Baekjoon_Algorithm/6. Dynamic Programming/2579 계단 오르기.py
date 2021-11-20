# 문제 https://www.acmicpc.net/problem/2579
# 앞으로 어떤 계단을 밟을 것인가 -> 어떤 계단을 밟고 올라왔는가 라고 생각하기.
# 바로 한칸 전 n-1 계단을 밟고 온 경우, 세 칸 연속 밟고 올 수 없으므로 그 이전 계단은 n-3 번째 계단 
# 두칸 전 n-2 계단을 밟고 온 경우
# 위 두 경우 중 최댓값 
num = int(input())

data = [0]
for i in range(num):
  data.append(int(input()))

if num == 1 :
  print(data[1])
else :
# 해당 위치에서 최댓값 저장 
  result = [0] * (num + 1)
  result[1] = data[1]
  result[2] = data[1] + data[2]

  for i in range(3,num+1):
    result[i] = max(result[i-3]+data[i]+data[i-1], result[i-2] + data[i])

  print(result[num])