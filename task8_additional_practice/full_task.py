""" Реализовать на python:
- генератор
- декоратор
- итератор
- контекстный менеджер
"""


def countdown(num):
    """Generator 1"""
    print('Start')
    while num > 0:
        yield num
        num -= 1


a = countdown(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print()

# Generator 2
my_list = ['H', 'e', 'l', 'l', 'o']
gen_obj = (x for x in my_list)
for val in gen_obj:
    print(val)
print()

def gen(string):
    """ Generator 3"""
    for item in string:
        yield item
        print(item + "2")


b = gen("abcdefg")
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print()

def decorator_function(func):
    def wrapper():
        print('Декоратор')
        print('Оборачиваем: {}'.format(func))
        print('Выполняем функцию...')
        func()
        print('Вот так!')
    return wrapper


@decorator_function
def hello_world():
    print('Hello world!')


hello_world()
print()

def benchmark(func):
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))
    return wrapper


@benchmark
def fetch_webpage():
    import requests
    webpage = requests.get('https://google.com')


fetch_webpage()
print()


def converting(fnc):
    """converting our arguments to dict"""
    def wrapper(*args):
        dict1 = dict(fnc(*args))
        return f'New dictionary is: {dict1}'
    return wrapper


@converting
def zipp(lst1, lst2):
    """Zip two lists"""
    return zip(lst1, lst2)


print(zipp([1, 2, 3, 4], ['foo', 'boo', 'arr', 'grr']))
print()

def without_numbers(my_func):
    """Wrapper to delete all numbers from string"""
    def wrapper(argument):
        return ''.join(filter(str.isalpha, argument))
    return wrapper


@without_numbers
def some_text(text):
    return text


print(some_text("123fadfdakmfadkml1213kmavs12"))
print()


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




class Context:
    def __init__(self, name, how):
        self.file_name = open(name, how)

    def __enter__(self):
        return self.file_name

    def __exit__(self, exit_type, exit_value, exit_traceback):
        self.file_name.close()


with Context('Example.txt', "w") as file:
    file.write('My first context manager')
print(file.closed)
with Context('Example.txt', "r") as file:
    file_data = file.read()
print(file_data)
print(file.closed)