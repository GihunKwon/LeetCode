class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            c = word.index(ch)
            return word[0:c+1][::-1] + word[c+1:]
        return word