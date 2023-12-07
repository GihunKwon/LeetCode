class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ad = []
        bd = []
        for i in range(1,a+1):
            if a % i == 0:
                ad.append(i)
        for j in range(1,b+1):
            if b % j == 0:
                bd.append(j)
        return len(set(ad) & set(bd))
