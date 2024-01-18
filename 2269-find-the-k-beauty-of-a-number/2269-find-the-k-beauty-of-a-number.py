class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        answer = 0
        num = str(num)
        for i in range(len(num)-k+1):
            div = int(num[i:i+k])
            if div != 0 and int(num) % div == 0:
                answer += 1
        return answer