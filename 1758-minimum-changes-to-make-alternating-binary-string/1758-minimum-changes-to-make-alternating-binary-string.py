class Solution:
    def minOperations(self, s: str) -> int:
        answer = 0
        s = [i for i in s]
        for i in range(1,len(s)):
            if s[i-1] == s[i]:
                answer += 1
                if s[i-1] == '1':
                    s[i] = '0'
                elif s[i-1] == '0':
                    s[i] = '1'
        return min(answer,len(s)-answer)