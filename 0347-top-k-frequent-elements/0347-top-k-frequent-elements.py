class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        cnt = Counter(nums)
        for key,val in cnt.most_common(k):
            answer.append(key)
        return answer