# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

'''
# 시간 초과 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0 
        
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                ans = max(ans, prices[j]- prices[i])
        
        return ans 
'''        

# 완전 탐색할 경우 시간 복잡도가 O(n^2)이므로 최솟값 변수를 두어, O(N)으로 풀이 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 숫자들 중 최솟값을 저장할 변수 
        min_p = max(prices)
        ans = 0
        for a in prices :
            ans = max(ans, a- min_p)
            
            # 최솟값 갱신 
            if a < min_p :  
                min_p = a
                
        return ans 