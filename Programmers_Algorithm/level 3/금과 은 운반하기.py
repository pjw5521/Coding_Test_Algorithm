# https://programmers.co.kr/learn/courses/30/lessons/86053
def solution(a, b, g, s, w, t):
    answer = int(10**16)
    left = 0 
    right = int(10**16)
    
    while left <= right :
        mid = (left + right) // 2 
        gold = 0 
        silver = 0 
        total = 0 
        
        # 각 도시 별 
        for i in range(len(g)):
            # 왕복할 수 있는 최대 횟수 
            cnt = mid // (t[i] * 2)
            # 편도로 이동가능하면 + 1 
            if mid % ( t[i] * 2 ) >= t[i]:
                cnt += 1 
            
            c_gold = 0
            c_silver = 0
            # 옮길 수 있는 최대 금과 은 구하기 
            if w[i] * cnt <= g[i] :
                c_gold = w[i] * cnt 
            else:
                c_gold = g[i]
                
            if w[i] * cnt <= s[i]:
                c_silver =  w[i] * cnt 
            else:
                c_silver = s[i]
        
            # 도시에서 옮길 수 있는 광물의 총합의 최댓값 구하기 
            if w[i] * cnt <= s[i] + g[i] :
                total += w[i] * cnt 
            else:
                total += s[i] + g[i]
            
            # 옮길 수 있는 금과 은의 총합     
            gold += c_gold 
            silver += c_silver
            
        # 옮길 수 있는 최대 금의 개수가 옮겨야하는 금의 개수보다 크면 
        # 옮길 수 있는 최대 은의 개수가 옮겨야하는 은의 개수보다 크면 
        # 옮길 수 있는 최대 광물의 개수가 옮겨야하는 광물의 개수보다 크면     
        if gold >= a and silver >= b and total >= a+b:
            # 최소 시간 갱신 
            answer = min(answer,mid)
            right = mid -1
        else:
            left = mid + 1 
            
    return answer

a = 10
b = 10
g = [100]
s = [100]
w = [7]
t = [10]
print(solution(a,b,g,s,w,t))