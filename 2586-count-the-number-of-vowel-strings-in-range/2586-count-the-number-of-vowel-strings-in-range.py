class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        answer = 0
        vowel = ['a','e','o','u','i']
        for i in words[left:right+1]:
            if i[0] in vowel and i[-1] in vowel:
                answer += 1
        return answer
            