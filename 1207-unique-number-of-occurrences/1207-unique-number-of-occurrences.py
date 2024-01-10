class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        answer = []
        for i in set(arr):
            if arr.count(i) not in answer:
                answer.append(arr.count(i))
            else:
                return False
                
        print(answer)
        return True