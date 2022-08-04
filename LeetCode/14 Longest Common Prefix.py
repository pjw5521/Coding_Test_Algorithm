# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # 길이가 가장 짧은 단어 기준으로 비교하면 됨 
        strs.sort(key = len)
        result = ''
        for i in range(len(strs[0])):
            # 길이가 가장 짧은 단어의 한 글자씩 늘려도 가능한지 확인 
            find = strs[0][i]
            for j in range(len(strs)):
                if find == strs[j][i] :
                    # 모든 단어의 prefix 해당 
                    if j == len(strs)-1:
                        # 점점 늘려감 
                        result += find 
                else :
                    return result 
                
        return result 
            
            