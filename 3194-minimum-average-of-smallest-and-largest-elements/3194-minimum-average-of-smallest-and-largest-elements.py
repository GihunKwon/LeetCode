class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        while len(nums)>0:
            a = min(nums)
            b = max(nums)
            nums.remove(a)
            nums.remove(b)
            averages.append((a+b)/2)
        return min(averages)