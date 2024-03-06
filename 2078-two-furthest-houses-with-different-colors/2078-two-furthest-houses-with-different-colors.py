class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        answer = 0
        for i,color in enumerate(colors):
            if color != colors[0]:
                answer = max(answer,i)
            if color != colors[-1]:
                answer = max(answer,len(colors)-1-i)
        return answer