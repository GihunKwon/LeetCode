class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        answer = float('inf')
        for i in range(len(blocks)-k+1):
            b = blocks[i:i+k]
            white = b.count('W')
            answer = min(answer,white)
        
        return answer