# https://programmers.co.kr/learn/courses/30/lessons/92335

# n의 base 진법으로 나타낸 수 구하기 
def cal(n, base):
    ans = ''
    while n > 0 :
        n, r = divmod(n, base)
        ans += str(r)
    
    return ans[::-1]
    
def solution(n, k):
    # 변환한 수 
    c_num = cal(n,k)
    # 소수의 개수 
    cnt = 0 
    # '0' 기준으로 나누기 
    num_list = c_num.split('0')
    
    for num in num_list:
        # 연속된 0의 경우 ''가 나타날 수 있으므로 
        if num == '':
            continue 
        
        num = int(num)
        
        # 소수 판별하기 
        result = True 
        if num == 1 :
            continue 
        
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                result = False 
                break 
            
        if result :
            cnt += 1 
            
    return cnt 

n = 110011
k = 10
print(solution(n,k))