class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        # answer = 0
        # for i in words:
        #     if i[::-1] in words and i[::-1] != i:
        #         answer += 1
        #         words.remove(i[::-1])
        # return answer
        return int(sum(1 for i in words if i[::-1] in words and i[::-1] != i)/2)