class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        answer = []
        while nums:
            alice = min(nums)
            nums.remove(alice)
            bob = min(nums)
            nums.remove(bob)

            answer.append(bob)
            answer.append(alice)
        return answer
