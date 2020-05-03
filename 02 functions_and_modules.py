def my_dick(k): # functions
    print(k)
    return k
    print("This won't be printed")

z = my_dick
print(z(50))

import random as ran
from math import pi as pi_number

value = ran.randint(1,6)
pi = pi_number

print(value, pi_number)


def apply_twice(func,arg):
    return func(func(arg))


def add_five(x):
    print("lalala")
    return x+5


print(apply_twice(add_five,10))

