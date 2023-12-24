class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        sl = s.lower()
        l = len(s) // 2
        a = sl[:l]
        b = sl[l:]
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        return sum(1 for i in a if i in vowel) == sum(1 for j in b if j in vowel)