class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        element = list(set(nums))
        for num in element:
            if nums.count(num) > len(nums)//2:
                return num
        
    