class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        answer = 0
        for i in nums:
            if i + diff in nums and i + diff + diff in nums:
                answer += 1
        return answer