# https://programmers.co.kr/learn/courses/30/lessons/77885
def solution(numbers):
    answer = []
   
    for i in numbers:
        # 짝수일 땐 맨 뒤를 1로 바꿈, 즉 1 더하기 
        if i % 2 == 0:
            answer.append(i+1)
        else :
            # 모두 1로 구성되어있을 때를 위해 제일 앞에 0 추가 
            b_num = ['0']
            # 이진수 변환 
            b_num.extend(list(map(str,bin(i)[2:])))
            
             # 뒤에서부터 0 만나면 1로 바꾸고 그 뒤에 숫자 0으로 바꾸기 
            for i in range(len(b_num)-1, -1, -1):
                if b_num[i] == '0':
                    b_num[i] = '1' 
                    b_num[i+1] = '0'
                    b_num = '0b' + "".join(b_num)
                    # 10진수 변환 
                    b_num = int(b_num, 2)
                    
                    answer.append(b_num)
                    break
                            
    return answer
    
n = [2,7]
print(solution(n))