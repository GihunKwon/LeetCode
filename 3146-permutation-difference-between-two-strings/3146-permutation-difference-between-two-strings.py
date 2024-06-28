class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        answer = 0
        for s_index,char in enumerate(s):
            t_index = t.index(char)
            answer += abs(s_index - t_index)
        return answer