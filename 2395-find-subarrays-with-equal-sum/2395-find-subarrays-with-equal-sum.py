class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        answer = []
        for i in range(len(nums)-1):
            s = sum(nums[i:i+2])
            if s in answer:
                return  True
            answer.append(s)
        return False