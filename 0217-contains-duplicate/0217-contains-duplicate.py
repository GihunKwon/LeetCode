class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = Counter(nums)
        for i,j in dict.items():
            if j > 1:
                return True
                break
        return False