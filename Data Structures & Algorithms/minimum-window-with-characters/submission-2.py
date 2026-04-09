class Solution:
    def minWindow(self, s: str, t: str) -> str:
        shortest_substring = ""
        if len(t) > len(s):
            return shortest_substring
        t_map = {}
        for i in range(len(t)):
            t_map[t[i]] = t_map.get(t[i], 0) + 1
        l = 0
        s_map = {}
        for r in range(len(s)):
            s_map[s[r]] = s_map.get(s[r],0) + 1
            if r - l + 1 >= len(t):
                while all( s_map.get(char, 0) >= t_map[char] for char in t_map):
                        current_substring = s[l:r + 1]
                        if len(shortest_substring) > len(current_substring) or not shortest_substring:
                            shortest_substring = current_substring
                        s_map[s[l]] -= 1
                        if s_map[s[l]] == 0:
                            del s_map[s[l]]
                        l += 1
        
        return shortest_substring




