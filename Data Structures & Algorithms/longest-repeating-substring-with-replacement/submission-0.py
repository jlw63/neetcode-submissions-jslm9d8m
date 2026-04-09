class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        frequency = {}
        max_length = 0
        for r in range(len(s)):
            frequency[s[r]] = frequency.get(s[r], 0) + 1
            highest_freq = max(frequency.values())
            dif_letter = (r - l + 1) - highest_freq
            if dif_letter > k:
                frequency[s[l]] -= 1
                l += 1
            else:
                if max_length < (r-l + 1):
                    max_length = r - l + 1
        return max_length


        
        