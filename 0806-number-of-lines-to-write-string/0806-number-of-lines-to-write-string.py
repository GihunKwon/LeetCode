class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        line = 1
        width = 0
        for i in s:
            i = ord(i)-97
            if widths[i] + width <= 100:
                width += widths[i]
            else:
                line += 1
                width = widths[i]
        return [line,width]