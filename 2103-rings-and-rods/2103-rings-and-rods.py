class Solution:
    def countPoints(self, rings: str) -> int:
        answer = 0
        dict = defaultdict(list)
        for i in range(0,len(rings),2):
            dict[rings[i+1]].append(rings[i])
        for j,k in dict.items():
            if set(k) == {'B', 'G', 'R'}:
                answer += 1
        return answer