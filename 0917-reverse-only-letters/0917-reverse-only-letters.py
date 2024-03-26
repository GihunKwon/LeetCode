class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        answer = [i for i in s if i.isalpha()]
        ans = ''
        for i in s:
            if i.isalpha():
                ans += answer.pop()
            else:
                ans += i
        return ans