class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        special_char = [i for i in '!@#$%^&*()-+']
        if len(password) < 8:
            return False
        upper = False
        lower = False
        digit = False
        special = False
        previous = ''
        for i,char in enumerate(password):
            if char.isupper():
                upper = True
            elif char.islower():
                lower = True
            elif char.isdigit():
                digit = True
            elif char in special_char:
                special = True
            if i == 0:
                previous = char
            else:
                if previous == char:
                    return False
                else:
                    previous = char
        return upper == lower == digit == special