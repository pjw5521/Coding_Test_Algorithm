#https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    answer = True
    # 정렬 
    phone_book.sort()
    for i in range(len(phone_book)-1):
        # 다음 숫자가 현재 숫자보다 더 길면, (같은 숫자는 존재 x)
        if len(phone_book[i]) < len(phone_book[i+1]):
            # 다음 숫자의 접두어 비교 
            if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
                answer = False 
                break
    return answer