class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        sym = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(len(s)-1):
            if sym[s[i]] < sym[s[i+1]]:
                answer -= sym[s[i]]
            else:
                answer += sym[s[i]]
        return answer + sym[s[-1]]

        # answer = 0
        # sym = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        # for i in range(len(s)-1):
        #     if sym[s[i]] < sym[s[i+1]]:
        #         answer += (sym[s[i+1]] - sym[s[i]])
        #     else:
        #         answer += sym[s[i]]
        # return answer + sym[s[-1]]
        
        # 이거 문제가 16번 줄에서 발생함
        # CM의 경우 900만 더하면 되는데, 뒤에서 M 1000을 한번 더 더함
        # 쉽게 말하면 (M-C) + M 이 되어버림
        # 그러면 뒤의 경우는 건드릴 수가 없으니 앞의 경우를 건드리면 된다
        # 즉 앞의 계산에서 M이 안더해지고, -C만 발생하면 됨
        # 그러면 (sym[s[i+1]] - sym[s[i]]) 대신에 -= sym[s[i]]을 넣으면 된다
