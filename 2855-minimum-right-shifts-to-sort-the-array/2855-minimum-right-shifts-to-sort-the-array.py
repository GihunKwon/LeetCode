class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        if nums == sorted(nums):
            return 0
        else:
            answer = 0
            for i in range(len(nums)):
                nums = nums[-1:] + nums[:-1]
                answer += 1
                if nums == sorted(nums):
                    return answer
        return -1