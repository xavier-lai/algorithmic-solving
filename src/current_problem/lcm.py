from .gcd import find_gcd


def find_lcm(first_int: int, second_int: int):
    return int(first_int * second_int / find_gcd(first_int, second_int))
