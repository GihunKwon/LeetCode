class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        answer = []
        for i,j in nums:
            answer += range(i,j+1)
        return len(set(answer))