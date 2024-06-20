class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        answer = []
        for i,num in enumerate(nums):
            if num == target:
                answer.append(abs(i-start))
        return min(answer)