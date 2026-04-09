class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        result = set()
        longest_s = 0
        for r in range(len(s)):
            while s[r] in result:
                result.remove(s[l])
                l += 1
            result.add(s[r])
            if longest_s < len(result):
                longest_s = len(result)
        return longest_s
