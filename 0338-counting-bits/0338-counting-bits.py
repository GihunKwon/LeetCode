class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []
        for i in range(n+1):
            i = i.bit_count()
            answer.append(i)
        return answer