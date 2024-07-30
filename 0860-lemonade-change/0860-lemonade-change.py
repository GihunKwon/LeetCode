class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dict = defaultdict(int)
        for i in bills:
            if i == 5:
                dict[5] += 1

            elif i == 10:
                if dict[5] >= 1:
                    dict[5] -= 1
                    dict[10] += 1
                else:
                    return False

            else:
                if dict[10] >= 1 and dict[5] >= 1:
                    dict[5] -= 1
                    dict[10] -= 1
                elif dict[5] >= 3:
                    dict[5] -= 3
                else:
                    return False

        return True