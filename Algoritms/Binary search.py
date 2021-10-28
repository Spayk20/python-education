"""Module for binary search algorithm"""


def binary_search(sequence, item):
    """Binary search for sorted list
    Args: sequence:list, item: int
    Return: index: int"""
    first_index = 0
    last_index = len(sequence) - 1
    while first_index <= last_index:
        mid_index = (first_index + last_index) // 2
        if item == sequence[mid_index]:
            return mid_index
        if item > sequence[mid_index]:
            first_index = mid_index + 1
        else:
            last_index = mid_index - 1
    return None


print(binary_search([3, 5, 7, 8, 10, 12, 19], 12))