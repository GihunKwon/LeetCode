class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        div,mod = divmod(time,n-1)
        if div % 2 == 0:
            return mod + 1
        else:
            return n - mod