class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        answer = -1
        cnt = 0
        for i in set(nums):
            if i % 2 == 0:
                i_cnt = nums.count(i)
                if i_cnt > cnt:
                    cnt = i_cnt
                    answer = i
                elif i_cnt == cnt:
                    answer = min(answer,i)
        return answer