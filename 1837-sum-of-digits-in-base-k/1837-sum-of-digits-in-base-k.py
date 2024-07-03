class Solution:
    def sumBase(self, n: int, k: int) -> int:
        num = ''
        while n > 0:
            n,mod = divmod(n,k)
            num += str(mod)
        num = num[::-1]
        
        answer = 0
        for i in num:
            answer += int(i)
        
        return answer