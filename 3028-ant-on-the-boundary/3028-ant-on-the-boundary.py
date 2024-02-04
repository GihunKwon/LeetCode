class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        answer = 0
        boundary = 0
        for num in nums:
            boundary += num
            if boundary == 0:
                answer += 1
        return answer