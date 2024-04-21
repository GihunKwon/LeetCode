class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if numOnes >= k:
            return k
        else:
            if numOnes + numZeros >= k:
                return numOnes
            else:
                total = numOnes + numZeros
                return numOnes + (k-total)*-1