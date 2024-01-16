class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        answer = 0
        cnt = 0
        for i in set(nums):
            if nums.count(i) > cnt:
                answer = nums.count(i)
                cnt = nums.count(i)
            elif nums.count(i) == cnt:
                answer += nums.count(i)
                cnt = nums.count(i)
        return answer