class Solution:
    def similarPairs(self, words: List[str]) -> int:
        answer = 0
        for i,j in combinations(words,2):
            if set(i) == set(j):
                answer += 1
        return answer