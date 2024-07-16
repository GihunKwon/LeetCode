class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = []
        answer = []
        k = 0
        for i in range(len(nums)):
            if nums[i] >= 1:
                seen = [nums[i]] + seen
                k = 0
            else:
                k += 1
                if k > len(seen):
                    answer.append(-1)
                else:
                    answer.append(seen[k-1])
        return answer