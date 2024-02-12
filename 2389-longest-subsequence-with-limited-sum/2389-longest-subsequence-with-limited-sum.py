class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # answer = [0]*len(queries)
        # for i,query in enumerate(queries):
        #     total = []
        #     for num in sorted(nums):
        #         if num <= query and num + sum(total) <= query:
        #             total.append(num)
        #     answer[i] = len(total)
        # return answer
        
        answer = [0]*len(queries)
        total = [0]
        for num in sorted(nums):
            total.append(total[-1] + num)
        
        for i,query in enumerate(queries):
            answer[i] = bisect.bisect_right(total,query) - 1

        return answer
