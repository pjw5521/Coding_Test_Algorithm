#https://programmers.co.kr/learn/courses/30/lessons/64065
def solution(s):
    s = s[2:-2]
    s = s.split('},{')
    s.sort(key=len)
    answer = []
    for i in s:
      tmp = i.split(',')
      for num in tmp:
        if int(num) not in answer:
          answer.append(int(num))

    return answer