class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        subs = []
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                subs.append(s[i:j])
        nice = []
        for sub in subs:
            if set(sub) == set(sub.swapcase()):
                nice.append(sub)
        return max(nice,key=len,default='')