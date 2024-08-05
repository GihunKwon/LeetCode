class Solution:
    def reformat(self, s: str) -> str:
        alpha = []
        digit = []
        for i in s:
            if i.isdigit():
                digit.append(i)
            else:
                alpha.append(i)

        if abs(len(alpha)-len(digit)) > 1:
            return ''
        
        if len(alpha) < len(digit):
            alpha,digit = digit,alpha
        answer = ''
        for i in range(len(s)):
            if i % 2 == 0:
                answer += alpha.pop()
            else:
                answer += digit.pop()
        return answer