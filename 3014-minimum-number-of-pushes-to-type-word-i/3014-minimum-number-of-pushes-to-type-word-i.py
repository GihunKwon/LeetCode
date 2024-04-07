class Solution:
    def minimumPushes(self, word: str) -> int:
        answer = 0
        l = len(word)
        row = 1

        while l:
            if l > 8:
                answer += 8*row
                l -= 8
                row += 1
            else:
                answer += l*row
                break
        return answer