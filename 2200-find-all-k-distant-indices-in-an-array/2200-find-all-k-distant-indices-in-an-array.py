class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        answer = []
        for i in range(len(nums)):
            if nums[i] == key:
                for j in range(i-k,i+k+1):
                    if j >= 0 and j < len(nums):
                        answer.append(j)
        return list(set(answer))