class Solution:
    def isThree(self, n: int) -> bool:
        answer = 0
        for i in range(1,n+1):
            if n % i == 0:
                answer += 1
            if answer > 3:
                return False
        return answer == 3