class Solution:
    def makeFancyString(self, s: str) -> str:
        answer = s[:2]
        for i in range(2,len(s),1):
            if s[i-2] == s[i-1] == s[i]:
                continue
            answer += s[i]
        return answer