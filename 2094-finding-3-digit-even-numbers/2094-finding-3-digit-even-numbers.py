class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        answer = set()
        for i,j,k in permutations(digits,3):
            if i != 0 and k % 2 == 0:
                num = 100*i + 10*j + k
                answer.add(num)
        
        return sorted(answer) 