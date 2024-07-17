class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        answer = 0
        for i in set(word.lower()):
            if i.lower() in word and i.upper() in word:
                answer += 1
        return answer