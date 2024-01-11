class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        answer = []
        for i in range(len(nums)):
            total = [nums[i]]
            for j in range(i+1,len(nums)):
                if total[-1] < nums[j]:
                    total.append(nums[j])
                else:
                    answer.append(sum(total))
                    break
            answer.append(sum(total))
        return max(answer)