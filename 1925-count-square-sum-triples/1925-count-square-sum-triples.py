class Solution:
    def countTriples(self, n: int) -> int:
        answer = 0
        for a,b,c in combinations(range(1,n+1),3):
            if a**2 + b**2 == c**2:
                answer += 2
        return answer