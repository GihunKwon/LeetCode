class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dict = Counter(nums)
        
        answer = 0
        for i,cnt in dict.items():
            if i + 1 in dict:
                answer = max(answer, cnt + dict[i+1])
        return answer