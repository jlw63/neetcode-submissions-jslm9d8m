class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for n in s:
            d[n] = d.get(n,0) + 1
        for n in t:
            if n not in d:
                return False
            d[n] = d[n] - 1
            if d[n] == 0:
                del d[n]

        if len(d) == 0:
            return True
        else:
            return False
        