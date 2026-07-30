class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                else:
                    l += 1
                    r -= 1
            return True
        
        l,r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                left, right = isPalindrome(l,r-1), isPalindrome(l+1,r)
                if left:
                    r -= 1
                elif right:
                    l += 1
                else:
                    return False
            else:
                l += 1
                r -= 1
        return True
                


        


        