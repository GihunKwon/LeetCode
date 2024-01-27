class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        answer = 0
        start = bin(start)[2:]
        goal = bin(goal)[2:]
        if len(start) > len(goal):
            goal = ('0'*(len(start)-len(goal))) + goal
        elif len(start) < len(goal):
            start = ('0'*(len(goal)-len(start))) + start
            
        for i,j in zip(start,goal):
            if i != j:
                answer += 1

        return answer