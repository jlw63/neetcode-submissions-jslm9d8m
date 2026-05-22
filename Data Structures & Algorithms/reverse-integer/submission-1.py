class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        result = 0
        if x < 0:
            negative = True
            x = abs(x)
        while x:
            temp = x % 10
            result *= 10
            result += temp
            x = x//10
        if negative:
            result *= -1 
        
        if result < -2147483648 or  result > 2147483647:
            result = 0
        return result