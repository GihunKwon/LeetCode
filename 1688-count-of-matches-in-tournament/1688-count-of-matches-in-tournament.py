class Solution:
    def numberOfMatches(self, n: int) -> int:
        answer  = 0
        team = n
        while team > 1:
            if team % 2:
                answer += (team-1)/2
                team = ((team-1)/2) + 1
            else:
                answer += team/2
                team = team/2
        return int(answer)       