class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        answer = 0
        for i,j in combinations(range(len(nums)+1),2):
            sub = nums[:i] + nums[j:]
            if sub == sorted(sub) and len(sub) == len(set(sub)):
                answer += 1
        return answer