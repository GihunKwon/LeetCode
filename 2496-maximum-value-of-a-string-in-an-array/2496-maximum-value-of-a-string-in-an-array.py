class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        answer = 0
        for i in strs:
            if i.isnumeric():
                answer = max(answer,int(i))
            else:
                answer = max(answer,len(i))
        return answer