class Solution:
    def romanToInt(self, s: str) -> int:
        converter = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        exception_converter = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

        output = 0
        idx = 0
        while idx < len(s):
            roman_symbol = s[idx]
            to_add = converter[roman_symbol]
            if idx + 1 < len(s):
                next_roman_symbol = s[idx + 1]
                two_symbol = roman_symbol + next_roman_symbol
                two_symbol_converted = exception_converter.get(two_symbol, None)

                if two_symbol_converted is not None:
                    to_add = two_symbol_converted
                    idx += 1
            idx += 1
            output += to_add

        return output
