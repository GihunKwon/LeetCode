class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        for i in range(1,len(words)+1):
            if ''.join(words[:i]) == s:
                return True
        return False