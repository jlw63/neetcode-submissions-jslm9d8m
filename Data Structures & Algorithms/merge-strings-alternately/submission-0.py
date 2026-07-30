class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        counter = 0
        output = ""
        while (len(word1) -1  >= counter and len(word2) -1 >= counter):
            output += word1[counter]
            output += word2[counter]
            counter += 1
        if len(word1) -1  >= counter:
           output += word1[counter:]

        if len(word2) -1  >= counter:
            output += word2[counter:]
        return output
