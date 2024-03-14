class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        answer = 0
        for i in range(left,right+1):
            cnt = i.bit_count()
            if cnt == 1:
                pass
            else:
                for j in range(2,cnt):
                    if cnt % j == 0:
                        break
                else:
                    answer += 1
        return answer