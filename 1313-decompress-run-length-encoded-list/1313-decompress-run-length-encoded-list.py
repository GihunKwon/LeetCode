class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)//2):
            freq,val = nums[2*i],nums[2*i+1]
            while freq > 0:
                answer.append(val)
                freq -= 1
        return answer