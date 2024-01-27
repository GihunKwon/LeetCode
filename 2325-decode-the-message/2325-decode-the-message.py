class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        code = ''
        for i in key.replace(' ',''):
            if i not in code:
                code += i
        
        decode = ''
        for j in message:
            if j != ' ':
                num = code.index(j)
                decode += chr(97+num)
            else:
                decode += j
        return decode