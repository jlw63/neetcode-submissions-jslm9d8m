class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for i in s:
            hashmap[i] = hashmap.get(i, 0) + 1
        for i in t:
            if i not in hashmap:
                return False
            hashmap[i] -= 1
            if hashmap[i] == 0:
                del hashmap[i] 
        if not hashmap:
            return True
        return False
        