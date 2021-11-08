# 문제 325쪽 
# https://programmers.co.kr/learn/courses/30/lessons/60059

# 2차원 배열 90도로 회전하는 함수 
def rotate_a_matrix_by_90_degree(a):
  n = len(a)
  m = len(a[0])
  result = [ [0] * n for _ in range(m)]
  for i in range(n):
    for j in range(m):
      result[j][n-i-1]= a[i][j]
  return result 

# 중심 값이 모두 1인지 확인하는 함수 
def check(new_lock):
  n = len(new_lock) // 3 
  for i in range(n, n*2):
    for j in range(n, n * 2):
      if new_lock[i][j] != 1:
        return False
  
  return True


def solution(key,lock):
  n = len(lock)
  m = len(key)
  # 3배 확장
  new_lock = [ [0] * n * 3 for _ in range(n*3) ]

  # 중심에 원래 lock 값 대입 
  for i in range(n):
    for j in range(n):
      new_lock[i+n][j+n] = lock[i][j]

# 회전 4번마다 
  for _ in range(4):
    key = rotate_a_matrix_by_90_degree(key)
    
    for x in range(n*2):
      for y in range(n*2):
    
        for i in range(m):
          for j in range(m):
            new_lock[x+i][y+j] += key[i][j]

        if check(new_lock) == True:
          return True
        
        for i in range(m):
          for j in range(m):
            new_lock[x+i][y+j] -= key[i][j]
  
  return False

