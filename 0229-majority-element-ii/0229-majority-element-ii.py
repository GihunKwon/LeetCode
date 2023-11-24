class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # answer = []
        # for i in nums:
        #     if nums.count(i) > len(nums) // 3:
        #         answer.append(i)
        # return list(set(answer))
        answer = []
        num = Counter(nums)
        for i,j in num.items():
            if j > len(nums) / 3:
                answer.append(i)
        return answer
