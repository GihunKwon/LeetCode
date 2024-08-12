class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        nums = [i+1 for i in range(len(matrix))]
        for i in matrix:
            if sorted(i) != sorted(nums):
                return False
        
        matrix = zip(*matrix)
        for i in matrix:
            if sorted(i) != sorted(nums):
                return False
        return True