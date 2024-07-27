class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dict = {}
        for i in set(nums):
            dict[i] = nums.count(i)
        
        answer = 0
        for i in dict:
            if i + 1 in dict:
                answer = max(answer, dict[i] + dict[i+1])
        return answer