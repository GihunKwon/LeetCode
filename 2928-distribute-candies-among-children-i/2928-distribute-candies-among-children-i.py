class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        answer = 0
        for i in range(n+1):
            for j in range(n+1):
                for k in range(n+1):
                    if (i+j+k) == n:
                        if i <= limit and j <= limit and k <= limit:
                            answer += 1
        return answer