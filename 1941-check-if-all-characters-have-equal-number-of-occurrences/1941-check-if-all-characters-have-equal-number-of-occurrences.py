class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        answer = []
        for i in set(s):
            answer.append(s.count(i))
        return len(set(answer)) == 1