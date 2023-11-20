class Solution:
    def numberOfSteps(self, num: int) -> int:
        answer = 0
        while num > 0:
            if num % 2:
                num -= 1
            else:
                num /= 2
            answer += 1
            num = num
        return answer