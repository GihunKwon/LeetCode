class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        answer = []
        # while nums:
        #     alice = min(nums)
        #     nums.remove(alice)
        #     bob = min(nums)
        #     nums.remove(bob)

        #     answer.append(bob)
        #     answer.append(alice)
        # return answer
        nums.sort()
        for i in range(0,len(nums),2):
            answer.append(nums[i+1])
            answer.append(nums[i])
        return answer