class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Wasita car or a cat I saw?
        s = s.lower()
        s = s.replace(" ", "")
        s =  ''.join(filter(str.isalnum, s))
        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
            

        