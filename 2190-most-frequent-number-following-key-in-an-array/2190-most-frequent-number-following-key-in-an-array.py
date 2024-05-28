class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        dict = defaultdict(int)
        for i in range(len(nums)-1):
            if nums[i] == key:
                dict[nums[i+1]] += 1
        
        return max(dict,key=dict.get)