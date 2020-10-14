import random
win_or_loose_count = 0
tries_range = 1
numb_gates = 7


for i in range(1,tries_range+1):

    x = {}

    for i in range(1,numb_gates+1):
        x[i] = False

    x[random.randint(1,numb_gates)] = True

    for i in x:
        print(x[i])

    picked_gate = random.randint(1,numb_gates)
    opened_gate = random.randint(1,numb_gates)

    if opened_gate == picked_gate or x[opened_gate] == True:
        while opened_gate == picked_gate or x[opened_gate] == True:
            opened_gate = random.randint(1,numb_gates)

    for i in x:
        if x[i] == True or i == opened_gate:
            None
        else:
            x[i] = None

    if x[picked_gate]:
        win_or_loose_count += 1

    print("---------------------------------------------")
    for i in x:
        print(x[i])


