class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = sorted([i*i for i in nums])
        return answer