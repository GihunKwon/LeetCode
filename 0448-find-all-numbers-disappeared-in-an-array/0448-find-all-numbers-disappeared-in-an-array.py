class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        answer = []
        dict = {}
        for i in range(1,len(nums)+1):
            dict[i] = 0
        for j in nums:
            dict[j] += 1
        
        for k,l in dict.items():
            if l == 0:
                answer.append(k)
        return answer