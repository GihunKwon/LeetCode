class Solution:
    def minimumChairs(self, s: str) -> int:
        answer = []
        chair = 0
        for i in s:
            if i == 'E':
                chair += 1
                answer.append(chair)
            else:
                chair -= 1
        return max(answer)