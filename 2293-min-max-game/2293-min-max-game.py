class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            newNums = []
            for i in range(0,len(nums),2):
                if len(newNums) % 2 == 0:
                    a = min(nums[i],nums[i+1])
                    newNums.append(a)
                else:
                    b = max(nums[i],nums[i+1])
                    newNums.append(b)
            nums = newNums
        return nums[0]