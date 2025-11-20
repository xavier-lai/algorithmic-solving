class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        substring_position = {i: str() for i in range(numRows)}
        position = 0
        direction = 1

        for ch in s:
            substring_position[position] += ch

            if position == 0:
                direction = 1
            elif position == numRows - 1:
                direction = -1

            position += direction

        output = str()
        for i in range(numRows):
            output += substring_position[i]

        return output
