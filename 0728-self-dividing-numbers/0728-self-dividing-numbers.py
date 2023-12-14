class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        answer = []
        for i in range(left,right+1):
            ch = False
            for j in str(i):
                if int(j) != 0 and i % int(j) == 0:
                    ch = True
                else:
                    ch = False
                    break
            if ch:
                answer.append(i)
        return answer