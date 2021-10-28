"""Module for quicksort algorithm"""


def q_split(sequence):
    pivot = sequence.pop()
    left = []
    right = []
    for element in sequence:
        if element >= pivot:
            right.append(element)
        else:
            left.append(element)
    left.append(pivot)
    return left, right


def quick_sort(sequence):
    parts = [sequence]
    while not all(len(a) == 1 for a in parts):
        print(parts)
        new_parts = []
        for part in parts:
            if len(part) == 1:
                new_parts.append(part)
                continue
            left, right = q_split(part)
            if len(right) == 0:
                right.append(left.pop())
            new_parts.append(left)
            new_parts.append(right)
        parts = new_parts
    return list(map(lambda x: x[0], parts))