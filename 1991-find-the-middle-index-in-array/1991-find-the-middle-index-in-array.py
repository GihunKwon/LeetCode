class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        answer = -1
        for i in range(len(nums)):
            if i == 0:
                if sum(nums[1:]) == 0:
                    return i
            elif i == len(nums) -1:
                if sum(nums[:-1]) == 0:
                    return i
            else:
                if sum(nums[:i]) == sum(nums[i+1:]):
                    return i
        return answer