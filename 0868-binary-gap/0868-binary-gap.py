class Solution:
    def binaryGap(self, n: int) -> int:
        if n.bit_count() == 1:
            return 0
        else:
            ans = []
            n = bin(n)[2:]
            for i,num in enumerate(n):
                if num == '1':
                    ans.append(i+1)
        number = 0
        for i in range(len(ans)-1):
            number = max(number,ans[i+1]-ans[i])
        return number