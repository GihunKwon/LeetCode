class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        answer = [0,0]
        for i,num in enumerate(bin(n)[2:][::-1]):
            if num == '1':
                if i % 2 == 0:
                    answer[0] += 1
                else:
                    answer[1] += 1
        return answer