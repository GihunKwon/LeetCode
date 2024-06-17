class Solution:
    def longestPalindrome(self, s: str) -> int:
        answer = 0
        odd = 0
        for i in set(s):
            if s.count(i) % 2 == 0:
                answer += s.count(i)
            elif s.count(i) % 2 == 1:
                answer += s.count(i) - 1
                odd += 1
        if odd:
            return answer + 1
        else:
            return answer
            