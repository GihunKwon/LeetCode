class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 0:
            return 'x'*(n-1) + 'y'
        if n % 2 == 1:
            return 'x'*n