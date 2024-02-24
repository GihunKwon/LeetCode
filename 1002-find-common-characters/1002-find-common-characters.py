class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dict = Counter(words[0])
        for i in words:
            dict &= Counter(i)
        return list(dict.elements())

        # answer = []
        # word1 = set(words[0])
        # for i in word1:
        #     freq = min([word.count(i) for word in words])
        #     answer += [letter] * freq
        # return answer