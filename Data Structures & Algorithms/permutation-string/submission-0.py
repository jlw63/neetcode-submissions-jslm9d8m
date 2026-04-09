class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = {}
        s2_window = {}
        if len(s1)>len(s2):
            return False
        for i in range(len(s1)):
            s1_freq[s1[i]] = s1_freq.get(s1[i],0) + 1
        l = 0
        for r in range(len(s2)):
            s2_window[s2[r]] = s2_window.get(s2[r],0) + 1
            if r - l + 1 == len(s1):
                if s1_freq == s2_window:
                    return True
                s2_window[s2[l]] -= 1
                if s2_window[s2[l]] == 0:
                    del s2_window[s2[l]]
                l += 1
        return False

        
            


        