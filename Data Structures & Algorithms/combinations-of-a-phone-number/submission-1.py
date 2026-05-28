class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",
        }
        res = []
        cur =[]

        def backtrack(i):
            if len(cur) == len(digits):
                res.append("".join(cur))
                return

            cur_digit = digits[i]
            cur_letters = phone[cur_digit]
            for letters in cur_letters:
                cur.append(letters)
                backtrack(i+1)
                cur.pop()
        if digits == "":
            return res
        backtrack(0)
        return res