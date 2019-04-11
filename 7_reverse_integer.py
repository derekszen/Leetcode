class Solution:
    # Given 32 bit integer, x, reverse integer
    # using 8 bit lookup table

    def reverse(self, x: int) -> int:
        result = -int(str(-x if x < 0 else x)[::-1]) if x < 0 else int(str(-x if x < 0 else x)[::-1])
        if (result > 2 ** 31 or result < -(2 ** 31) - 1):
            return 0
        return result
