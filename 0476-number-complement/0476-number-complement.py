class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        binary = binary.replace('1','2')
        binary = binary.replace('0','1')
        binary = binary.replace('2','0')
        
        return int(binary,2)