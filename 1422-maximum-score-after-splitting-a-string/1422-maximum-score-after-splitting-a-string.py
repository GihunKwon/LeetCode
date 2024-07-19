class Solution:
    def maxScore(self, s: str) -> int:
        answer = 0
        for i in range(1,len(s)):
            left = s[:i].count('0')
            right = s[i:].count('1')
            answer = max(answer,left+right)
        return answer