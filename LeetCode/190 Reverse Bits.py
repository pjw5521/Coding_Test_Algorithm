# https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        # 앞에  0b 제거 
        tmp = bin(n)[2:]
        
        # 길이가 32 될때까지 앞에 0 붙이기 
        while len(tmp) < 32 :
            tmp = '0' + tmp
        
        # 뒤집은 수 반환
        return int(tmp[::-1],2)