
def my_func(f,arg):
    return f(arg)


a = my_func(lambda x: 2*x*x,5)
print(a)
print(lambda x: 2*x*x)
print((lambda x: 2*x*x)(5))


def add_five(x):
    return x + 5


nums = [311,7,11,15,75,100,15325]
result = list(map(add_five,nums)) # or..
result = list(map(lambda x: x+5,nums))
result = list(filter(lambda x: x%5 == 0,result))
result = list(filter(lambda x: x%5 == 0,list(map(lambda x: x+5,nums))))
result = list(filter(lambda x: x%5 == 0,nums))

print(result)


def countdown_timer():
    i = 10
    while i > 0:
        yield i
        i -= 1


for i in countdown_timer():
    print(i)


def decor(func):
    def wrap():
        print("------------------")
        func()
        print("------------------")
    return wrap


def print_text():
    print("sdjfhdskjfhsdk")


decorated = decor(print_text)
decorated()


def factorial(x):
    if x == 1:
        return 1
    else:
        print(x)
        return x * factorial(x-1)


print(factorial(5))
