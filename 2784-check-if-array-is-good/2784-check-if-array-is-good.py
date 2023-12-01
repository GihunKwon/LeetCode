class Solution:
    def isGood(self, nums: List[int]) -> bool:
        sor = sorted(nums)
        if len(sor) < 2:
            return False
        return sor[-1] == sor[-2] and sor[:-1] == list(range(1,len(sor)))



        