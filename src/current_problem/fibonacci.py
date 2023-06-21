def get_fibonacci_list(number_element: int):
    fibonacci_list = []
    first_int, second_int = 1, 1
    for _ in range(number_element - 1):
        fibonacci_list.append(first_int)
        first_int, second_int = second_int, first_int + second_int
    return fibonacci_list
