#https://programmers.co.kr/learn/courses/30/lessons/12949
'''
행렬의 곱셈 

arr1[l][n] * arr2[n][m] = arr3[l][m] 
첫째 행렬 열의 개수와 둘째 행렬 행의 개수가 일치해야 곱셈 가능 
새롭게 만들어진 행렬곱은 첫째 행렬 행의 개수와 둘째 행렬 열의 개수를 가진다 

'''
def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1)) ]

    for i in range(len(arr1)):
        
        num = arr1[i]

        for j in range(len(arr2[0])):
            result = 0
            for k in range(len(num)):
                
                result += arr1[i][k] * arr2[k][j]
           
            answer[i][j] = result
                
    return answer

