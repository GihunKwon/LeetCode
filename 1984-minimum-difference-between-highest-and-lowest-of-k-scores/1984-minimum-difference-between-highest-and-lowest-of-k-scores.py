class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        if len(nums) == 1:
            return 0
        
        answer = float('inf')
        for i in range(len(nums)-k+1):
            sub = nums[i:i+k]
            diff = max(sub) - min(sub)
            answer = min(answer,diff)
        return answer