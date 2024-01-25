class Solution:
    def countAsterisks(self, s: str) -> int:
        answer = 0
        for i,string in enumerate(s.split('|')):
            if i % 2 == 0:
                answer += string.count('*')
        return answer