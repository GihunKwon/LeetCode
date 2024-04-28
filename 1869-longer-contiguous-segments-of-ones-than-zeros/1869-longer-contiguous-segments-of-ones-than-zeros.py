class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        zero,one = 0,0
        cur_zero,cur_one = 0,0

        for i in s:
            if i == '1':
                cur_one += 1
                cur_zero = 0
            else:
                cur_one = 0
                cur_zero += 1

            one = max(cur_one,one)
            zero = max(cur_zero,zero)
        
        return one > zero