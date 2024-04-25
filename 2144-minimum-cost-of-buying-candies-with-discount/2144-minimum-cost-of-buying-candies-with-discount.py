class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        answer = 0
        cost.sort(reverse=True)
        for i,num in enumerate(cost):
            i += 1
            if i % 3 != 0:
                answer += num
        return answer