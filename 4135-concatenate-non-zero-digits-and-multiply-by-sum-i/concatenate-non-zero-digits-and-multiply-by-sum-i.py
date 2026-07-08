class Solution(object):
    def sumAndMultiply(self, n):
        count = 0
        digit_sum = 0
        num = 0

        while n > 0:
            temp = n % 10
            digit_sum += temp

            if temp != 0:
                num += temp * (10 ** count)
                count += 1

            n //= 10

        return digit_sum * num