favorite_numbers = [6, 57, 4, 7, 68, 95]
my_iterator = iter(favorite_numbers)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print()


class SecPow:
    """Class that pow numbers"""
    def __init__(self, length):
        self.number = 1
        self.max = length

    def __iter__(self):
        return self

    def __next__(self):
        if self.number > self.max:
            raise StopIteration
        res = self.number ** 2
        self.number += 1
        return res


number = SecPow(5)
for i in number:
    print(i)