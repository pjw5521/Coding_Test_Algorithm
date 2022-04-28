# https://programmers.co.kr/learn/courses/30/lessons/77886
def solution(s):
    answer = []
   
    for st in s:
    	#'110'의 개수 
        cnt = 0 
        # 110 을 제거한 문자열 저장할 배열 
        stack = []
        for i in st:
            # 0이면 앞에 두글자 1, 1 인지 확인 
            if i == '0':
                if stack[-2:] == ['1', '1']:
                	# '110' 개수 증가 
                    cnt +=1 
                    # 1, 1 빼내기 
                    stack.pop()
                    stack.pop()
                # 110 아니면 그냥 추가 
                else:
                    stack.append(i)
            # 1은 그냥 추가 
            else :
                stack.append(i)
           
        # 110 없으면 그대로 추가 
        if cnt == 0 :
            answer.append(st)  
       # 110을 제거하고 남은 문자열이 없으면 110 개수 만큼 추가 
        elif not stack:
            stack = cnt * ['1','1','0']
            answer.append("".join(stack))
        else:
            idx = len(stack) -1     
            
            # 0의 위치 찾기 
            for i in range(idx, -1, -1):
                if stack[i] == '0':
                    idx = i 
                    break
                    
            # 0이 없으면 제일 앞에 추가 
            if stack[idx] == '1':
                stack = ['1','1','0'] * cnt + stack 
            # 0이 있으면 
            else :
                # 0이 제일 뒤에 위치하면 
                if idx == len(stack)-1 :
                	# 제일 뒤에 추가 
                    stack = stack + ['1','1','0'] * cnt
                # 사이에 있는 0이면 사이에 추가 
                else:
                    stack = stack[:idx+1] + ['1','1','0'] * cnt + stack[idx+1:]
                        
            # 정답 넣기 
            answer.append("".join(stack))
        
    return answer
    
# 스택이 비어있을 때 
s = ["110", "100111100", "0111111010"]
print(solution(s))