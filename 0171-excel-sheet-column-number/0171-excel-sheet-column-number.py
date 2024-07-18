class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        l = len(columnTitle)-1
        answer = 0
        for i in columnTitle:
            char = ord(i) - 64
            answer += char * (26**l)
            l -= 1
        return answer