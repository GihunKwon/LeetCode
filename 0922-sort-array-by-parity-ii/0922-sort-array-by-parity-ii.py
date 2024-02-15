class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        answer = [0]*len(nums)
        even = 0
        odd = 1
        for num in nums:
            if num % 2 == 0:
                answer[even] = num
                even += 2
            else:
                answer[odd] = num
                odd += 2
        return answer