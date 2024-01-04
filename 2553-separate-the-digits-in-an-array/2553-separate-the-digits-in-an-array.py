class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        a = ''.join(map(str,nums))
        for i in a:
            answer.append(int(i))
        return answer