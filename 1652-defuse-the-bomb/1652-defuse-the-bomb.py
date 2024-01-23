class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        answer = [0]*len(code)
        if k > 0:
            for i in range(len(code)):
                for j in range(1,k+1):
                    answer[i] += code[(i+j)%len(code)]
        if k == 0:
            return answer
        if k < 0:
            for i in range(len(code)):
                for j in range(1,abs(k)+1):
                    answer[i] += code[i-j]
        return answer