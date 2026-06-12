class Solution(object):
    def reverse(self, x):
        negative = x < 0
        x = abs(x)

        rev = 0

        while x > 0:
            digit = x % 10
            rev = rev * 10 + digit
            x = x // 10

        if negative:
            rev = -rev

        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev