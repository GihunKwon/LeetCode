class Solution:
    def makeGood(self, s: str) -> str:
        answer = []
        for i in s:
            if answer and answer[-1] == i.swapcase():
                answer.pop()
            else:
                answer.append(i)
        return ''.join(answer)
            