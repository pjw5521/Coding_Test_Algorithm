# 문제 361쪽
# https://programmers.co.kr/learn/courses/30/lessons/42889
# 둘 다 예제 코드도 틀림. 왜 인지 모르겠다..

# 답지 풀이 
def solution(N, stages):
    answer = []
    length = len(stages)

    # 스테이지 번호를 1부터 N까지 증가시키며
    for i in range(1, N + 1):
        # 해당 스테이지에 머물러 있는 사람의 수 계산
        count = stages.count(i)
        
        # 실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count / length
        
        # 리스트에 (스테이지 번호, 실패율) 원소 삽입
        answer.append((i, fail))
        length -= count

    # 실패율을 기준으로 각 스테이지를 내림차순 정렬
    answer = sorted(answer, key=lambda t: t[1], reverse=True)
    
    # 정렬된 스테이지 번호 반환
    answer = [i[0] for i in answer]
    return answer

# 내 풀이

def solution(N, stages):
    result = []
    n = len(stages)

    for i in range(1,N+1):
      cnt = stages.count(i)
      if n == 0:
        result.append((i, 0))
      else: 
        fail = cnt / n 
        result.append((i, fail))
      n -= cnt
    
    result.sort(key = lambda x : -x[1])
    answer = [ i[0] for i in result]

    return answer