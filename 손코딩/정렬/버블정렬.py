# 앞에서부터 인접한 두수를 비기ㅛ하며 정렬해나가는 방법 
# O(n^2)s
array = [9,8,7,6,5,4,3,2,1]

def bubble(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[i]
        
bubble(array)
print(array)