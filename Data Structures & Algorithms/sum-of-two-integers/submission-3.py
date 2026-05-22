class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while b:
            add = (a^ b) & mask
            carry = ((a & b)<<1) & mask
            a = add
            b = carry

        return a if a <= 0x7FFFFFFF else ~(a ^ mask)