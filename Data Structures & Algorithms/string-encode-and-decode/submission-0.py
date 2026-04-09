class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            length = str(len(s))
            encoded += length + "#" + s
        return encoded    

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.find("#",i)
            length = int(s[i:j])
            start = j + 1
            result.append(s[start:start + length])
            i = j + length + 1
        return result
