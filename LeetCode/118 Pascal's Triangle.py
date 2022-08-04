# https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        dp = [ [0] * (i+1) for i in range(numRows)]
        
        if numRows == 1 :
            dp[0][0] = 1 
        else :
            dp[0][0] = 1 
            dp[1][0] = 1 
            dp[1][1] = 1 
        
            for i in range(2,numRows):
                for j in range(i+1):
                    if j == 0 :
                        dp[i][j] = dp[i-1][j]
                    elif j == i-1 :
                        dp[i][j] = dp[i-1][j-1]
                    else :
                        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        
        return dp 