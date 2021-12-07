#https://programmers.co.kr/learn/courses/30/lessons/17681
def solution(n, arr1, arr2):
    answer = [[0]*n for _ in range(n)]
    map1 = []
    map2 = []
    result = []
    for i in arr1 :
        real = bin(i)[2:]
        real = real.zfill(n)
        map1.append(str(real))

    for i in arr2 :
        real = bin(i)[2:]
        real = real.zfill(n)
        map2.append(str(real))

    for i in range(n):
        for j in range(n):
                if map1[i][j] =='0' and map2[i][j] =='0':
                    answer[i][j] = " "
                else:
                     answer[i][j] = "#"
    for i in range(n):
        result.append("".join(answer[i]))
    return result 