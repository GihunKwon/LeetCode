class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dict = {}
        for i in range(len(names)):
            dict[heights[i]] = names[i]
        sor = sorted(heights,reverse=True)
        answer = []
        for j in sor:
            answer.append(dict[j])
        return answer