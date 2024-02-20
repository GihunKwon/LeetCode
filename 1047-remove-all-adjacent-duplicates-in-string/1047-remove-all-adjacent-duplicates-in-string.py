class Solution:
    def removeDuplicates(self, s: str) -> str:
        answer = []

        for i in s:
            if len(answer) == 0:
                answer.append(i)
            else:
                if answer[-1] == i:
                    answer.pop()
                else:
                    answer.append(i)
        return ''.join(answer)