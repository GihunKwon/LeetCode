class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        answer = 0
        for i,j in combinations(words,2):
            if j.startswith(i) and j.endswith(i):
                answer += 1
        return answer