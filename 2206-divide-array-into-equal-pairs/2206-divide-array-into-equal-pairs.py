class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums_s = set(nums)
        for i in nums_s:
            if nums.count(i) % 2 == 1:
                return False
                break
        return True