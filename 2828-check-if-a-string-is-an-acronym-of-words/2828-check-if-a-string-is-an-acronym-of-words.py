class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        answer = ''
        for i in words:
            answer += i[0]
        return answer==s