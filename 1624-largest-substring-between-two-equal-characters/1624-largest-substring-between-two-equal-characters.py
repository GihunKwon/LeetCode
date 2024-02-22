class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        answer = -1
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i] == s[j]:
                    answer = max((j-i-1),answer)
        return answer
    