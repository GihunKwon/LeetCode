class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        divisors = set(divisors)
        answer = 0
        div = 0
        for i in divisors:
            num = 0
            for j in nums:
                if j % i == 0:
                    num += 1
            if num > div:
                answer = i
                div = num
            if num == div:
                answer = min(answer,i)

        if div == 0 and answer == 0:
            return min(divisors)
        return answer
            