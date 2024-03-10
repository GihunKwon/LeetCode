class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        answer = 0
        for i,num in enumerate(nums):
            i = bin(i)[2:]
            total = 0
            for j in i:
                if j == '1':
                    total += 1
            if total == k:
                answer += num
        return answer