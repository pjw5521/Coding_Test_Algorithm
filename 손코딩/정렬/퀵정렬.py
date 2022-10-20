# 분할정복 알고리즘 
# 추가적인 메모리 공간 필요없음 
# pivot을 설정하고 그 기준으로 정렬 

array = [8,4,6,2,9,1,3,7,5]

def quick(array):
    if len(array) <= 1 :
        return array 
        
    pivot = len(array) // 2 
    right, p_array, left = [], [], []

    for value in array : 
        if value < array[pivot] :
            right.append(value)
        elif value > array[pivot]:
            left.append(value)
        else :
            p_array.append(value)
    
    return quick(right) + quick(p_array) + quick(left)
    
array = quick(array)
print(array)