class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        collection = set()
        num = 0
        while sorted(collection) != list(range(1,k+1)):
          if not nums:
            break
          p = nums.pop()
          if p <= k:
            collection.add(p)
          num += 1
        return num