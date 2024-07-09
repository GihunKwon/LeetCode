class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        if k == len(s):
            return s
        elif k > len(s):
            k = k % len(s)
        return s[k:] + s[:k]