class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        answer = float(inf)
        for i in target:
            answer = min(answer,s.count(i)//target.count(i))
        
        return answer