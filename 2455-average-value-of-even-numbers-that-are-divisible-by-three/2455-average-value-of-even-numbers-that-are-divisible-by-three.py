class Solution:
    def averageValue(self, nums: List[int]) -> int:
        answer = []
        for i in nums:
            if i % 6 == 0:
                answer.append(i)
        return sum(answer) // len(answer) if len(answer) > 0 else 0