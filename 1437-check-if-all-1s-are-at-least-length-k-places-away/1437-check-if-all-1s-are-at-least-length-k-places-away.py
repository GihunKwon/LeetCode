class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        answer = []
        for i,num in enumerate(nums):
            if num == 1:
                answer.append(i)
        
        for j in range(len(answer)-1):
            if answer[j+1] - answer[j] -1 < k:
                return False
        return True