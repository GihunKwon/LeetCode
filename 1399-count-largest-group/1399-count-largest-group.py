class Solution:
    def countLargestGroup(self, n: int) -> int:
        answer = {}
        
        for i in range(1,n+1):
            i = sum(map(int,str(i)))
            
            if i not in answer:
                answer[i] = 1
            else:
                answer[i] += 1

        m = max(answer.values())
        
        return sum(1 for i in answer.values() if i == m)