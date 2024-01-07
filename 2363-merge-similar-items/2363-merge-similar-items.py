class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        answer = defaultdict(int)
        for i in items1+items2:
            answer[i[0]] += i[1]
        return sorted(answer.items())