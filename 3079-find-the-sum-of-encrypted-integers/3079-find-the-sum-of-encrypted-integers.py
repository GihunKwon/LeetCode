class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] >= 10:
                num = 0
                for j in str(nums[i]):
                    num = max(num,int(j))
                num = int(str(num) * len(str(nums[i])))
                nums[i] = num
        return sum(nums)