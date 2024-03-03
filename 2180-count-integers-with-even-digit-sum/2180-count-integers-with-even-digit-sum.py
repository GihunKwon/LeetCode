class Solution:
    def countEven(self, num: int) -> int:
        answer = 0
        for i in range(1,num+1):
            total = 0
            for j in str(i):
                total += int(j)
            if total % 2 == 0:
                answer += 1
        return answer