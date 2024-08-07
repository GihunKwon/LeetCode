class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        target = ord(target)-97
        letters = [ord(i)-97 for i in letters]
        
        for i in sorted(letters):
            if i > target:
                return chr(i+97)

        return chr(sorted(letters)[0]+97)