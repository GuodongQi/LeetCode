class Solution:
    def divide(self, dividend: 'int', divisor: 'int') -> 'int':

        MAX = 2147483647
        MIN = -MAX - 1
        pos = 1
        if dividend < 0 < divisor or dividend > 0 > divisor:
            pos = 0
        # if abs(dividend)>=
        r = 0
        divisor = abs(divisor)
        dividend = abs(dividend)

        def div(my_divident, my_divisor):
            result = 1
            while my_divident - my_divisor >= 0:
                result <<= 1
                my_divisor <<= 1
            result >>= 1
            my_divisor >>= 1
            my_divident = my_divident - my_divisor
            return result, my_divident

        while dividend > 0:
            result, dividend = div(dividend, divisor)
            r += result

        if not pos:
            r = - r
        if r < MIN:
            r = MIN
        if r > MAX:
            r = MAX
        return r


s = Solution()
print(s.divide(-15, 3))
