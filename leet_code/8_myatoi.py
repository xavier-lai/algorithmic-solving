class Solution:
    def myAtoi(self, s: str) -> int:
        min_int32 = -(2**31)
        max_int32 = (2**31) - 1

        s = s.strip()

        if len(s) == 0:
            return 0

        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
            sign = 1
        else:
            sign = 1

        s = s.lstrip("0")
        integer = 0
        for ch in s:
            if ch.isdigit():
                integer = (integer * 10) + int(ch)

                if sign * integer < min_int32:
                    return min_int32
                if sign * integer > max_int32:
                    return max_int32
            else:
                break
        return sign * integer
