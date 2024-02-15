class Solution:
    def fib(self, n: int) -> int:
        a,b = 1,1
        if n == 0:
            return 0
        if n in (1,2):
            return a
        for i in range(1,n):
            a,b = b, a+b
        return a
        