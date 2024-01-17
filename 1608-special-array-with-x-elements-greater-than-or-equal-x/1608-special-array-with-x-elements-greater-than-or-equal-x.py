class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums = sorted(nums,reverse=True)
        for i in range(len(nums)):
            x = i + 1
            if nums[i] >= x:
                if i == (len(nums)-1):
                    return x
                    break
                if nums[i+1] < x:
                    return x
                    break
        return -1