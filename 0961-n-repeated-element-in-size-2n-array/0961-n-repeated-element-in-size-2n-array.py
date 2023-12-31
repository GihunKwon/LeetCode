class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        answer = 0
        l = len(nums)
        num = set(nums)
        for i in num:
            if nums.count(i) == l//2:
                answer += i
                break
        return answer