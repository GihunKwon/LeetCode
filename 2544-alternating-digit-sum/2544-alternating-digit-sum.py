class Solution:
    def alternateDigitSum(self, n: int) -> int:
        answer = 0
        for i,num in enumerate(str(n)):
            if i % 2 == 0:
                answer += int(num)
            else:
                answer -= int(num)
        return answer