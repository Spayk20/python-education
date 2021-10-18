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
        return f'My new dict is: {dict1}'
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