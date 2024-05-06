class Solution:
    def countElements(self, nums: List[int]) -> int:
        if len(set(nums)) == 1:
            return 0
        nums.sort()
        l = len(nums)-2
        a = nums.count(nums[0])
        b = nums.count(nums[-1])
        return l - (a+b-2)