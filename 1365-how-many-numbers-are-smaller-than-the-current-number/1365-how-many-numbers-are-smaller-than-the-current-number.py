class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer = []
        for i in nums:
            ans = 0
            for j in nums:
                if i > j:
                    ans += 1
            answer.append(ans)
        return answer