class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        r_s = s[::-1]
        for i in range(len(s)-1):
            substr = s[i:i+2]
            if substr in r_s:
                return True
        return False