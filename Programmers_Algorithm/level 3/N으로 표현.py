#https://programmers.co.kr/learn/courses/30/lessons/42895
'''dp 풀이 '''
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

''' dfs로도 풀이 가능 '''
ans = int(1e9)

def dfs(n, cnt, num, number):
    
    global ans
    
    # 사용한 횟수가 최솟값보다 크면 중단 
    if ans < cnt :
        return 
    
    # 사용한 횟수가 8보다 크면 중단 
    if cnt > 8 :
        return 
    
    # 만들어진 숫자가 구하고자 하는 숫자이면 
    if num == number:
        # 사용한 횟수 최솟값 갱신 
        ans = min(ans, cnt)
        return 
     
    # 연속된 숫자    
    next_num = 0 
    
    # 최소 연산 횟수 8까지 반복 
    for i in range(8):
        # 연속된 숫자만들기 
        next_num = next_num*10 + n 
        # 더하기 연산 
        dfs(n, cnt + 1 + i, num + next_num, number)
        # 빼기 연산 
        dfs(n, cnt + 1 + i, num - next_num, number)
        # 곱하기 연산 
        dfs(n, cnt + 1 + i, num * next_num, number)
        # 나누기 연산 
        dfs(n, cnt + 1 + i, num / next_num, number)

def solution(N, number):

    # 사용할 숫자, 사용한 횟수, 현재 값, 만들 숫자 
    dfs(N, 0, 0, number)
    
    # 8보다 적게 사용해서 만들 수 없다면 
    if ans == int(1e9):
        return -1
    else:    
        return ans