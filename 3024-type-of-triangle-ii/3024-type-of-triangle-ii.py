class Solution:
    def triangleType(self, nums: List[int]) -> str:
        num = set(nums)
        l = len(num)
        
        if sum(sorted(nums)[:2]) <= sorted(nums)[2]:
            return 'none'
        if l == 1:
            return 'equilateral'
        elif l == 2:
            return 'isosceles'
        else:
            return 'scalene'
