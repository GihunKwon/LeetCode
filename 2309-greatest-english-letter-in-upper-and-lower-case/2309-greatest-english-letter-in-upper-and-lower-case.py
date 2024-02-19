class Solution:
    def greatestLetter(self, s: str) -> str:
        answer = []
        for i in set(s):
            if i.lower() in s and i.upper() in s:
                answer.append(i.upper())
        return sorted(answer)[-1] if answer else ''