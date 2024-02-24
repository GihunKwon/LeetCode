class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        answer = []
        vowel = ['a','e','i','o','u']
        for i,word in enumerate(sentence.split(' ')):
            if word[0].lower() in vowel:
                word += 'ma' + ('a' * (i+1))
                answer.append(word)
            else:
                word += word[0]
                word = word[1:]
                word += 'ma' + ('a' * (i+1))
                answer.append(word)
        return ' '.join(answer)