#https://programmers.co.kr/learn/courses/30/lessons/43105
def solution(triangle):

    for i in range(1, len(triangle)):
      for j in range(i+1):
        # 왼쪽 끝일 때 
        if j == 0 :
          triangle[i][j] += triangle[i-1][j]
        # 오른쪽 끝일 때 
        elif j == i:
          triangle[i][j] += triangle[i-1][j-1]
        # 가운데일 때 
        else:
        # 더 큰 수 더하기 
          if triangle[i-1][j-1] > triangle[i-1][j]:
            triangle[i][j] += triangle[i-1][j-1]
          else :
            triangle[i][j] += triangle[i-1][j]
   
    return max(triangle[-1])

