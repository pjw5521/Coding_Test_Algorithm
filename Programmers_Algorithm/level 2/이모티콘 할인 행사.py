# https://school.programmers.co.kr/learn/courses/30/lessons/150368
from itertools import product

def solution(users, emoticons):
    answer = []
    sale = [10,20,30,40]
    # 중복 순열 
    products = list(product(sale, repeat= len(emoticons)))

    for pro in products:
    	# 사용자별 구매 금액 
        cost = [0] * len(users)
        # 이모티콘 판매액 
        total = 0
        
        # 각 이모티콘 별 사용자가 구매하는지 안하는지 
        for i in range(len(emoticons)):
            for j in range(len(users)):
            	# 할인율이 더 크면 
                if pro[i] >= users[j][0]:
                	# 구매 금액 갱신 
                    cost[j] += emoticons[i] - int(emoticons[i] * pro[i] * 0.01)
                    # 판매액 갱신 
                    total += emoticons[i] - int(emoticons[i] * pro[i] * 0.01)
        
		# 이모티콘 플러스 가입자 수 
        people = 0 
        
        for i in range(len(users)):
        	# 사용자가 지정한 금액보다 많이 구매했으면 
            if cost[i] >= users[i][1]:
				# 구매를 취소 
                total -= cost[i]
                # 이모티콘 플러스 가입 
                people += 1 

        answer.append([people, total])
	
    # 이모티콘 플러스 가입자 수와 판매액이 큰 순으로 정렬 
    answer.sort(reverse=True)
    
    return answer[0]