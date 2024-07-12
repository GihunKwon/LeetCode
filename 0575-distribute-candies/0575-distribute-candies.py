class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        c = set(candyType)
        if len(c) >= (len(candyType)/2):
            return len(candyType)//2
        else:
            return len(c)