class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        first = ''
        second = ''
        target = ''
        for i in firstWord:
            first += str(ord(i) - 97)
        for j in secondWord:
            second += str(ord(j) - 97)
        for k in targetWord:
            target += str(ord(k) - 97)
        
        print(int(first),int(second),int(target))
        print(first,second,target)
        return int(first) + int(second) == int(target)