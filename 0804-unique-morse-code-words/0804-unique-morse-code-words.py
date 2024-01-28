class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alp = 'abcdefghijklmnopqrstuvwxyz'
        answer = ['']*len(words)
        for i,word in enumerate(words):
            for alpha in word:
                answer[i] += morse[alp.index(alpha)]
        return len(set(answer))