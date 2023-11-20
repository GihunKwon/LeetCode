class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        answer = 0
        for i in items:
            if ruleKey == 'type'and  i[0] == ruleValue:
                answer += 1
            elif ruleKey == 'color' and i[1] == ruleValue:
                answer += 1
            elif ruleKey == 'name' and i[2] == ruleValue:
                answer += 1
        return answer