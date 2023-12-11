class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        answer = []
        for i in rectangles:
            answer.append(min(i))
        return answer.count(max(answer))