# 문제 321쪽 
# https://www.acmicpc.net/problem/18406
N = input()

half_length = int(len(N)/2)

suma= 0
sumb = 0
for i in range(0,half_length) :
  suma += int(N[i])

for i in range(half_length,len(N)) :
  sumb += int(N[i])

if suma == sumb:
  print("LUCKY")
else:
  print("READY")