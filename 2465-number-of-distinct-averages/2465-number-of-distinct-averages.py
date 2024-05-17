class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        answer = []
        while nums:
            a = max(nums)
            b = min(nums)
            avg = (a+b)/2
            answer.append(avg)
            nums = nums[1:-1]
        return len(set(answer))