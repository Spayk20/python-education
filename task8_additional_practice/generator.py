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