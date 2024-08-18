class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = [i for i in s]
        for i in range(0,len(s),k+k):
            s[i:i+k] = s[i:i+k][::-1]
        
        return ''.join(s)