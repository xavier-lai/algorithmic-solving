class Solution:
    def naiveIsPalindrome(self, x: int) -> bool:
        x_str = str(x)
        x_reverse = x_str[::-1]

        return x_str == x_reverse

    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False

        reverse = 0
        classic = x
        while x > 0:
            last_digit = x % 10
            reverse = (reverse * 10) + last_digit
            x = x // 10
        return reverse == classic
