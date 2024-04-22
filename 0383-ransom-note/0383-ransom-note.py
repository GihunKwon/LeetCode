class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = defaultdict(int)
        for i in magazine:
            dict[i] += 1
        
        for j in ransomNote:
            if j in dict:
                dict[j] -= 1
                if dict[j] < 0:
                    return False
            else:
                return False
        return True