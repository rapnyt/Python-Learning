import math
desired_range = 10
x = list()
y = list()
for i in range(2, desired_range + 1):
    x.append(i)
    y.append(i)

for i in x:
    if i < math.sqrt(desired_range):
        for j in y:
            if i * j <= desired_range:
                try:
                    x.remove(i*j)
                except(ValueError):
                    None

for i in x:
    print(i)