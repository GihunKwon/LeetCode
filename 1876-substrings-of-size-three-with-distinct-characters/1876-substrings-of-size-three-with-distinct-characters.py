class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        answer = 0
        for i in range(2,len(s)):
            if len(set(s[i-2:i+1])) == 3:
                answer += 1
        return answer