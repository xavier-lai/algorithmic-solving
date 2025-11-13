class Solution:
    def reverse(self, x: int) -> int:
        max_int32 = 2**31 - 1
        min_int32 = -(2**31)

        sign = -1 if x < 0 else 1

        x_abs = abs(x)
        reversed = 0
        quotient = 1

        while quotient > 0:
            quotient, remainer = divmod(x_abs, 10)
            reversed = (10 * reversed) + remainer
            x_abs = quotient
            if reversed < min_int32 or reversed > max_int32:
                return 0
        return sign * reversed
