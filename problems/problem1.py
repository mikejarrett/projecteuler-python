# -*- coding: utf-8 -*-

def get_sum_of_numbers(numbers):
    """ Loop through a range of numbers. If the number is divisible by 
    3 or 5 add it to the list. Finally sum the list.

    :param numbers: range of numbers
    :return: Integer sum
    """
    return sum(
        number for number in numbers 
        if number % 3 == 0 or number % 5 == 0
    )
    
if __name__ == "__main__":
    result = (get_sum_of_numbers(range(1, 1000)))
    assert result == 233168
    print(result)