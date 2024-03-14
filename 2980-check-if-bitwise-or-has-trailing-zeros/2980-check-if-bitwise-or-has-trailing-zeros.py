class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        for i,j in combinations(nums,2):
            if bin(i|j)[2:].endswith('0'):
                return True
        return False