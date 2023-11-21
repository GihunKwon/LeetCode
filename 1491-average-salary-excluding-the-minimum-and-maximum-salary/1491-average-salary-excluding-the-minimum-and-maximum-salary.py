class Solution:
    def average(self, salary: List[int]) -> float:
        sort = sorted(salary)
        return sum(sort[1:-1]) / len(sort[1:-1])