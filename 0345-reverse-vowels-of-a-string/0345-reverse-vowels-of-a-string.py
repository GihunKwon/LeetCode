class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['i','a','e','o','u']
        vowel = [i for i in s if i.lower() in vowels]
        
        answer = ''
        for j in s:
            if j.lower() in vowels: 
                answer += vowel[-1]
                vowel.pop()
            else:
                answer += j
        return answer