class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        answer = 0
        for i in nums:
            if i % 3 == 0:
                continue
            elif i % 3 == 1:
                answer += 1
            elif i % 3 == 2:
                answer += 1
        return answer