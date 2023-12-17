class Solution:
    def totalMoney(self, n: int) -> int:
        answer = 0
        week = 1
        while n > 0:
            if n // 7 > 0:
                answer += sum(range(week,week+7))
                n -= 7
                week += 1
            elif n // 7 == 0:
                answer += sum(range(week, week+(n%7)))
                break
        return answer