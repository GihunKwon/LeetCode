class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        answer = [0,0]
        dict = Counter(nums)
        for i,j in dict.items():
            if j % 2 == 0:
                answer[0] += j//2
            else:
                answer[0] += j//2
                answer[1] += j%2
        return answer