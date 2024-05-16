class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        dict = defaultdict(int)
        for i in logs:
            for j in range(i[0],i[1]):
                dict[j] += 1
        
        answer = 0
        population = 0
        for i,j in dict.items():
            if j > population:
                population = j
                answer = i
            if j == population and answer > i:
                answer = i

        return answer