class Solution:
    def maxDepth(self, s: str) -> int:
        answer = []
        depth = 0
        for string in s:
            if string == '(':
                depth += 1
            elif string == ')':
                answer.append(depth)
                depth -= 1
        return max(answer) if answer else 0