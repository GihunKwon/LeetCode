class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split(' ')
        for i,s in enumerate(sentence):
            if s.startswith(searchWord):
                return i+1
        return -1