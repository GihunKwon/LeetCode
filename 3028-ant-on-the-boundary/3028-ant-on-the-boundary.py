class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        answer = 0
        cur = 0
        for i in nums:
            cur += i
            if cur == 0:
                answer += 1
        return answer