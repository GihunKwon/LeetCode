class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        answer = []
        min_num = [min(i) for i in matrix]
        max_num = [max(i) for i in zip(*matrix)]
        for i in min_num:
            if i in max_num:
                answer.append(i)
        return answer