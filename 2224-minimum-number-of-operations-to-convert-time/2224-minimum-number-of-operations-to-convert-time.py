class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        answer = 0
        cur = list(map(int,current.split(':')))
        cor = list(map(int,correct.split(':')))
        diff = 60*(cor[0]-cur[0]) + (cor[1]-cur[1])

        for i in [60,15,5,1]:
            div,mod = divmod(diff,i)
            answer += div
            diff = mod

        return answer