import math
desired_range = 100
x = list()

for i in range(2, desired_range + 1):
    x.append(i)

for i in x:
    if i*i < desired_range:
        for j in range(2, math.ceil(desired_range/i + 1)):
            try:
                x.remove(i*j)
            except(ValueError):
                None

for i in x:
    print(i)