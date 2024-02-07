class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words1 = [word for word in words1 if words1.count(word) == 1]
        words2 = [word for word in words1 if words2.count(word) == 1]
        return len(set(words1)&set(words2))