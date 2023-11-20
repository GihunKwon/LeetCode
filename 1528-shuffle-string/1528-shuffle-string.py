class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s_dict = {}
        answer = []
        for key,value in zip(indices,s):
            s_dict[key] = value
        for i in range(len(s)):
            answer += s_dict[i]
        return ''.join(answer)