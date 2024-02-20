class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # answer = []
        # for i in range(len(num)-2):
        #     if num[i] == num[i+1] and num[i+1] == num[i+2]:
        #         answer.append(num[i] * 3)
        # return sorted(answer)[-1] if answer else ''

        good = [str(i)*3 for i in range(9,-1,-1)]
        for i in good:
            if i in num:
                return i
        return ''
