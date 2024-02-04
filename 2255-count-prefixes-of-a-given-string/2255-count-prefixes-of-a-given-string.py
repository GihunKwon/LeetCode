class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        answer = 0
        for word in words:
            l = len(word)
            if word == s[:l]:
                answer += 1
        return answer