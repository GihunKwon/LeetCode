class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split(' ')
        answer = []
        for i in s:
            if i.isdigit():
                answer.append(int(i))
        return answer == sorted(answer) and len(set(answer)) == len(answer)