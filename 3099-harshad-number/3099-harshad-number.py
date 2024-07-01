class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        answer = sum(int(i) for i in str(x))
        return answer if x % answer == 0 else -1