class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer = []
        a = len(nums)//2
        for i in range(a):
            answer.append(nums[i])
            answer.append(nums[i+a])
        return answer