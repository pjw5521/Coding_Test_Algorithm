# https://www.acmicpc.net/problem/12015

# lower bound 
# num과 같거나 큰 가장 작은 인덱스 구하기 
def binary_search(arr, num):
    start = 0 
    end = len(arr) -1 
    
    while start <= end :
        mid = (start+end) // 2
        
        if arr[mid] >= num :
            end = mid -1 
        else:
            start = mid + 1 
    
    return start 
    
n = int(input())
data = list(map(int,input().split()))

max_list = []

for num in data:
    idx = binary_search(max_list, num)
    
    # 리스트의 최댓값보다 크므로 추가 
    if idx == len(max_list):
        max_list.append(num)
    # 해당 인덱스의 값을 업데이트 
    else:
        max_list[idx] = num
        
print(len(max_list))