class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l = len(s)
        answer = 0
        for i in range(l+1):
            for j in range(i+1,l+1):
                sub = s[i:j]
                for k in sub:
                    if sub.count(k) > 2:
                        break
                else:
                    answer = max(answer,len(sub))
        return answer