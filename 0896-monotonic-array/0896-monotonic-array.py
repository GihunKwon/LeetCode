class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = False
        decreasing = False
        
        for i in range(0, len(nums) - 1):
            num1 = nums[i]
            num2 = nums[i+1]
            
            if num1 < num2:
                if decreasing:
                    return False
                increasing = True
            if num1 > num2:
                if increasing:
                    return False
                decreasing = True
        
        return True