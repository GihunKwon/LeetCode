class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            answer = ''
            for i in range(0,len(s),k):
                total = 0
                num = s[i:i+k]
                for j in num:
                    total += int(j)
                answer += str(total)
            s = answer
        return s

                