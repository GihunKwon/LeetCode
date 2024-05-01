class Solution:
    def bitwiseComplement(self, n: int) -> int:
        n = bin(n)[2:]
        n = n.replace('1','2')
        n = n.replace('0','1')
        n = n.replace('2','0')
        
        return int(n,2)