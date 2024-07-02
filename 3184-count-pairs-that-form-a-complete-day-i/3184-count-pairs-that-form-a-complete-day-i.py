class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        answer = 0
        for i,j in combinations(hours,2):
            if (i + j) % 24 == 0:
                answer += 1
        return answer