class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        s_ = [s[i:i+k] for i in range(0,len(s),k)]
        if len(s_[-1]) < k:
            s_[-1] += fill* (k-len(s_[-1]))

        return s_