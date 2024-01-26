class Solution:
    def freqAlphabets(self, s: str) -> str:
        alp = ' abcdefghijklmnopqrstuvwxyz'
        answer = ''
        cur = 0
        while cur < len(s):
            if cur+2 < len(s) and s[cur+2] == '#':
                answer += alp[int(s[cur:cur+2])]
                cur += 3
            else:
                answer += alp[int(s[cur])]
                cur += 1
        return answer