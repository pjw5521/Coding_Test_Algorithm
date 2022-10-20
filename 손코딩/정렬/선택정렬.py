# 한 바퀴 돌때 가장 작은 값을 찾아 맨 앞과 교환하는 방식 
# O(n^2)
array = [8,4,6,2,9,1,3,7,5]

def selection(array):
    n = len(array)
    
    for i in range(n):
        max_index = i
        
        for j in range(i+1,n):
            if array[j] < array[max_index]:
                max_index = j 
            
        array[i], array[max_index] = array[max_index],array[i]
    
selection(array)
print(array)