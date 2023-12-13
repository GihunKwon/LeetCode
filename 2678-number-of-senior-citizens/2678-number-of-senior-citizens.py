class Solution:
    def countSeniors(self, details: List[str]) -> int:
        answer = 0
        for i in details:
            if int(i[-4:-2]) > 60:
                answer += 1
        return answer