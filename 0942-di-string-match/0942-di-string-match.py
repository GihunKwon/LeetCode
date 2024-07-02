class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        perm = [i for i in range(len(s)+1)]
        answer = []
        for i in s:
            if i == 'I':
                answer.append(perm[0])
                perm = perm[1:]
            else:
                answer.append(perm[-1])
                perm = perm[:-1]

        answer.append(perm[0])
        
        return answer