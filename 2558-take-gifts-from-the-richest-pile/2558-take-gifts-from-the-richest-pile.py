class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        second = 0
        while second != k:
            second += 1
            maxi = max(gifts)
            i = gifts.index(maxi)
            gifts[i] = int(maxi**0.5)
        return sum(gifts)