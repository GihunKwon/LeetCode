class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        answer = 0

        letter = s[0]
        c = 1
        for i in s[1:]:
            if i == letter:
                c += 1
            else:
                letter = i
                c = 1
            answer = max(c,answer)
        
        return answer
            