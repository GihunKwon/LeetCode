class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        answer = 0
        for i in range(len(strs[0])):
            alp = []
            for j in range(len(strs)):
                alp.append(strs[j][i])
            if alp != sorted(alp):
                answer += 1
        return answer