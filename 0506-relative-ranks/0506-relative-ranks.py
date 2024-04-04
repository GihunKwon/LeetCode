class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        scores = sorted(score,reverse=True)
        rank = {}
        ans = []
        for i,j in enumerate(scores):
            if i == 0:
                rank[j] = 'Gold Medal'
            elif i == 1:
                rank[j] = 'Silver Medal'
            elif i == 2:
                rank[j] = 'Bronze Medal'
            else:
                rank[j] = str(i+1)
        for i in score:
            ans.append(rank[i])
        return ans