class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #define values
        phone_map = {
        "2" : "abc",
        "3" : "def",
        "4" : "ghi",
        "5" : "jkl",
        "6" : "mno",
        "7" : "pqrs",
        "8" : "tuv",
        "9" : "wxyz"
        }
        cur = []
        res = []

        def backtrack(i):
            #basecase
            if len(digits) == 0:
                return
            if len(cur) == len(digits):
                   res.append("".join(cur))
                   return
            
            digit = digits[i]
            letters = phone_map[digit]
            for c in letters:
                cur.append(c)
                backtrack(i+1)
                cur.pop()
        backtrack(0)
        return res