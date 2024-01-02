class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        alp = 'abcdefghijklmnopqrstuvwxyz'
        s = list(s)
        for i in range(0,len(s)//2):
            if s[i] != s[-i-1]:
                s[i] = alp[min(alp.index(s[i]) , alp.index(s[-i-1]))]
                s[-i-1] = alp[min(alp.index(s[i]) , alp.index(s[-i-1]))]
        return ''.join(s)