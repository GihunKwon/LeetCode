class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        # answer = 0
        # for i in range(len(brackets)):
        #     if i == 0:
        #         if income <= brackets[i][0]:
        #             answer += income*brackets[i][1]/100
        #             break
        #         elif income > brackets[i][0]:
        #             answer += brackets[i][0] * brackets[i][1] / 100
        #             income -= brackets[i][0]
        #     else:
        #         if income <= brackets[i][0] - brackets[i-1][0]:
        #             answer += income * brackets[i][1] / 100
        #             break
        #         elif income > brackets[i][0] - brackets[i-1][0]:
        #             answer += (brackets[i][0] - brackets[i-1][0]) * brackets[i][1] / 100
        #             income -= (brackets[i][0] - brackets[i-1][0])
        # return answer

        answer = 0
        prev = 0
        for i,j in brackets:
            amount = i - prev
            if income <= amount:
                answer += income*(j)/100
                break
            else:
                answer += amount * j / 100
                income -= i-prev
                prev = i
        return answer