class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        total = 0
        while nums:
            if len(nums) == 1:
                total += nums[0]
                break
            total += int(str(nums[0]) + str(nums[-1]))
            nums.pop(0)
            nums.pop(-1)
        return total
