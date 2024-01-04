class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i,num in enumerate(sorted(nums)):
            if num == target:
                answer.append(i)
        return answer