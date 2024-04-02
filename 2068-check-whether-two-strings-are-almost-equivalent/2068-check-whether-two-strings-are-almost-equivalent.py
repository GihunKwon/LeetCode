class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        for i in set(word1):
            cnt_1 = word1.count(i)
            cnt_2 = word2.count(i)
            if abs(cnt_1 - cnt_2) > 3:
                return False
        for j in set(word2):
            cnt_1 = word1.count(j)
            cnt_2 = word2.count(j)
            if abs(cnt_1 - cnt_2) > 3:
                return False
        return True