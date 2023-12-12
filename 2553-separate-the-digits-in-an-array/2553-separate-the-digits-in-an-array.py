class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        all = ''.join(map(str,nums))
        for i in all:
            answer.append(int(i))
        return answer