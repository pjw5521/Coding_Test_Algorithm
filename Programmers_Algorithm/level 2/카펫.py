# https://programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
  # i*2 , j*2 의 합은 brown - 4 
  # i * j 곱은 yellow    
  # 결과값은 i+2, j+ 2 
  for i in range(1, brown):
    for j in range(1, brown):
      if i*2 + j*2 == brown-4 and i*j == yellow:
        if i > j:
          return [i+2,j+2]
        else:
          return [j+2,i+2]
