class Solution:
    def check(self, nums: List[int]) -> bool:
        l = len(nums)
        nums = 2 * nums
        for i in range(len(nums)-l):
            if nums[i:i+l] == sorted(nums[i:i+l]):
                return True
        return False