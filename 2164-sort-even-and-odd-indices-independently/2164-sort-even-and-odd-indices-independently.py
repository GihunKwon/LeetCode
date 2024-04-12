class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        answer = []
        odd = []
        even = []
        for i in range(1,len(nums),2):
            odd.append(nums[i])
        for j in range(0,len(nums),2):
            even.append(nums[j])
        odd.sort(reverse=True)
        even.sort()

        for a,b in zip(even,odd):
            answer.append(a)
            answer.append(b)
        if len(odd) != len(even):
            answer.append(even[-1])
        return answer