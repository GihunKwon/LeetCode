class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        answer = 0
        for word in words:
            l = 0
            for letter in word:
                if letter in chars and word.count(letter) <= chars.count(letter):
                    l += 1
            if l == len(word):
                answer += l
        return answer