class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        answer = 0
        points.sort()
        for i in range(1,len(points)):
            if points[i][0] - points[i-1][0] > answer:
                answer = points[i][0] - points[i-1][0]
        return answer