class Solution:
    def balancedStringSplit(self, s: str) -> int:
        answer = 0
        r = 0
        l = 0
        for i in s:
            if i == 'R':
                r += 1
            elif i == 'L':
                l += 1

            if r == l:
                answer += 1
                r = l = 0
        return answer