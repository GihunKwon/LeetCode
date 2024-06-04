class Solution:
    def maxSum(self, nums: List[int]) -> int:
        dict = defaultdict(list)
        answer = -1
        for num in nums:
            max_digit = int(max(str(num)))
            dict[max_digit].append(num)
        
        for num in dict:
            if len(dict[num]) > 1:
                dict[num].sort()
                max_num = dict[num][-1] + dict[num][-2]
                answer = max(answer,max_num)

        return answer