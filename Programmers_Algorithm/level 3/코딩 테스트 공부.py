# https://school.programmers.co.kr/learn/courses/30/lessons/118668
def solution(alp, cop, problems):
    answer = 0
    INF = int(1e9)

    # 목표값 
    max_alp = 0
    max_cop = 0 
	
    # 목표값 -> 문제들의 최대 코딩력 & 알고력 
    for problem in problems:
        max_alp = max(max_alp, problem[0])
        max_cop = max(max_cop, problem[1])

    # 현재 가지고 있는 알고력과 코딩력이 목표값보다 클 수 있으므로, 갱신 
    alp = min(max_alp, alp)
    cop = min(max_cop, cop)

    # dp[i][j] -> 알고력 i, 코딩력 j를 얻는데 걸리는 최단 시간
    dp = [[INF] * (max_cop +1)  for _ in range(max_alp+1) ]
    dp[alp][cop] = 0

    for i in range(alp, max_alp+1):
        for j in range(cop, max_cop+1):
            # 1의 시간을 들여 알고력 얻기 
            if i < max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1 )
            
            # 1의 시간을 들여 코딩력 얻기
            if j < max_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
                
            # 풀 수 있는 문제 중 하나 풀어서 보상으로 알고력, 코딩력 얻기 
            for alp_rep, cop_rep, alp_rwd, cop_rwd, cost in problems:
                # 풀 수 있으면 
                if i >= alp_rep and j >= cop_rep :
                    # 목표값을 넘어가지 않도록 갱신 
                    new_alp = min(i + alp_rwd, max_alp)
                    new_cop = min(j + cop_rwd, max_cop)
	
                	# 최솟값 갱신
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j] + cost)

    return dp[max_alp][max_cop]