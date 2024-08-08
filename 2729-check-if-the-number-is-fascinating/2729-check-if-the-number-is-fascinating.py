class Solution:
    def isFascinating(self, n: int) -> bool:
        n = str(n) + str(2*n) + str(3*n)

        if '0' in n:
            return False
        if len(n) > 9:
            return False
        for i in range(1,10):
            if str(i) not in n:
                return False
        return True