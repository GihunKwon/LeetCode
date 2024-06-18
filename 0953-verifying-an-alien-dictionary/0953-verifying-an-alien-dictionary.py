class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dict = {char : index for index,char in enumerate(order)}
        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            min_word = min(len(word1),len(word2))
            for j in range(min_word):
                if word1[j] != word2[j]:
                    if dict[word1[j]] > dict[word2[j]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True