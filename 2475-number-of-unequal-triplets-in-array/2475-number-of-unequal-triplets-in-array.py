class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        answer = 0
        for i,j,k in combinations(range(len(nums)),3):
            if i < j < k and nums[i] != nums[j] and nums[k] != nums[j] and nums[i] != nums[k]:
                answer += 1
        return answer