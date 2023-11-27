class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        answer = []
        for i in words:
           for j in i.split(separator):
                if j:
                   answer.append(j)
                else:
                    pass
        return answer