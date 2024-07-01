class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one_cnt = s.count('1')
        zero_cnt = s.count('0')
        if one_cnt < 2:
            return '0'*zero_cnt + '1'*one_cnt
        else:
            return '1'*(one_cnt-1) + '0'*zero_cnt + '1'