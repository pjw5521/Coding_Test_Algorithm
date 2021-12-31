#https://programmers.co.kr/learn/courses/30/lessons/42895
def solution(N, number):
    # dp[i]는 N을 i번 사용해서 나타낼 수 있는 수들의 집합 
    # N을 i번 반복한 수 넣기. i의 최솟값 8
    dp = [set([N*int('1'*i)]) for i in range(1,9)]

    for i in range(8):
      for j in range(i):
        for num1 in dp[j]:
           for num2 in dp[i-j-1]:
              dp[i].add(num1+num2)
              dp[i].add(num1-num2)
              dp[i].add(num1*num2)
              if num2 != 0 :
                dp[i].add(num1//num2)

      if number in dp[i]:
        return i+1
    return -1 