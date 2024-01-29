class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        answer = list(s)
        start = 0
        f = 0
        b = 0
        for i,par in enumerate(s):
            if par == '(':
                f += 1
            if par == ')':
                b += 1
            if f == b:
                f = 0
                b = 0
                answer[i] = ''
                answer[start] = ''
                start = i+1
        return ''.join(answer)