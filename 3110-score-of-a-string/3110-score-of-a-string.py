class Solution:
    def scoreOfString(self, s: str) -> int:
        answer = 0
        for i in range(len(s)-1):
            a = ord(s[i])
            b = ord(s[i+1])

            answer += abs(a-b)

        return answer