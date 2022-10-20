# 분할 정복 + 재귀
# o(nlogn)
array = [8,4,6,2,9,1,3,7,5]

def merge_sort(array):
    if len(array) < 2 :
        return array
        
    mid = len(array) // 2 
    low_arr = merge_sort(array[:mid])
    high_arr = merge_sort(array[mid:])
    
    merge_arr = []
    
    l_index = 0
    h_index = 0 
    
    while l_index < len(low_arr) and h_index < len(high_arr):
        if low_arr[l_index] < high_arr[h_index]:
            merge_arr.append(low_arr[l_index])
            l_index += 1 
        else :
            merge_arr.append(high_arr[h_index])
            h_index += 1 
        
    merge_arr += low_arr[l_index:]
    merge_arr += high_arr[h_index:]
    
    return merge_arr 

array = merge_sort(array)
print(array)
            
    