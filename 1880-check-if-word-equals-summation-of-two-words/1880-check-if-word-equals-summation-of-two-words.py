class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        alp = 'abcdefghij'
        first = ''
        second = ''
        target = ''
        for i in firstWord:
            first += str(alp.index(i))
        for j in secondWord:
            second += str(alp.index(j))
        for k in targetWord:
            target += str(alp.index(k))
        if int(first) + int(second) == int(target):
            return True
        else:
            return False