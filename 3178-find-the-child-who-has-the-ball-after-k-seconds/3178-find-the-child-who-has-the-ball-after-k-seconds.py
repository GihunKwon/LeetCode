class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        div,mod = divmod(k,n-1)
        if div % 2 == 0:
            return mod
        else:
            return n - 1 - mod