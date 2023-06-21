def find_gcd(first_int: int, second_int: int):
    if second_int > first_int:
        first_int, second_int = second_int, first_int
    if second_int == 0:
        return first_int

    return find_gcd(second_int, first_int % second_int)
