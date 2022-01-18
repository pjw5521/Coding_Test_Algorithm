# https://programmers.co.kr/learn/courses/30/lessons/12907
# dp 문제 
def solution(n, money):

  answer = [0] * (n+1)

  answer[0] = 1

  for coin in money:
    for price in range(coin, n+1):
      answer[price] += answer[price-coin]
  
  return (answer[n]) % 10000000007

