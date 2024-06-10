class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dict = Counter(nums)
        degree = max(dict.values())

        numbers = []
        for i in dict:
            if dict[i] == degree:
                numbers.append(i)
        
        answer = len(nums)
        for j in numbers:
            left = nums.index(j)
            right = len(nums) - nums[::-1].index(j)
            answer = min(answer,right-left)
        return answer