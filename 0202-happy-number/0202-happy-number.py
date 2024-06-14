class Solution:
    def isHappy(self, n: int) -> bool:
        current = n
        cnt = 0
        used = []

        while True:
            current = str(current)
            for i in current:
                cnt += int(i) ** 2
            if cnt == 1:
                return True
            if cnt in used:
                return False
            used.append(cnt)
            current = cnt
            cnt = 0