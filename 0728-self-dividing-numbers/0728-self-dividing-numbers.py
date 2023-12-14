class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        answer = []
        for i in range(left,right+1):
            bool = False
            for j in str(i):
                if j != '0' and i % int(j) == 0:
                    bool = True
                else:
                    bool = False
                    break
            if bool:
                answer.append(i)
        return answer

        