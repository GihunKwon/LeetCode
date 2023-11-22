class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alp = 'abcdefghijklmnopqrstuvwsyz'
        for i in alp:
            if i not in sentence:
                return False
        return True