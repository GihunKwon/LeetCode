class Solution:
    def maximum69Number (self, num: int) -> int:
        answer = ''
        for i in range(len(str(num))):
            if str(num)[i] == '9':
                answer += '9'
            else:
                answer += '9'
                answer += str(num)[i+1:]
                break
        return int(answer)