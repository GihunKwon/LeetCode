class Solution:
    def replaceDigits(self, s: str) -> str:
        answer = ''
        for i in range(len(s)):
            if s[i].isdigit():
                answer += chr(ord(s[i-1]) + int(s[i]))
            else:
                answer += s[i]
        return answer