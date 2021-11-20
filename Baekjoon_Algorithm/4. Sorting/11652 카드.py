# 문제 https://www.acmicpc.net/problem/11652
# 딕셔너리 사용 안하면 런타임 에러 
import sys
r = sys.stdin.readline

n = int(r())

card_dic= {}

# 숫자는 key, 등장 횟수가 value
for i in range(n):
  card = int(input())
  if card in card_dic:
    card_dic[card] += 1 
  else:
    card_dic[card] = 1 

# 숫자는 오름차순, 횟수는 내림차순으로 정렬 
result = sorted(card_dic.items(), key = lambda x: (-x[1],x[0]))

# 횟수가 가장 많으면서 그 중에서 가장 작은 수 
print(result[0][0])