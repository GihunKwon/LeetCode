class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(''.join(set(list(s))))