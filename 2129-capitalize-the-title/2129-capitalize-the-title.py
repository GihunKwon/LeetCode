class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.split()
        for i,word in enumerate(title):
            if len(word) < 3:
                title[i] = word.lower()
            else:
                title[i] = word.capitalize()
        return ' '.join(title)