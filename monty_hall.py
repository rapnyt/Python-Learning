import random
win_or_loose_count = 0

for i in range(1,2):

    x = {}

    for i in range(1,4):
        x[i] = False

    x[random.randint(1,3)] = True

    for i in x:
        print(x[i])

    picked_gate = random.randint(1,3)
    random_empty_gate_open = random.randint(1,3)
    while x[random_empty_gate_open] == True:
        random_empty_gate_open = random.randint(1, 3)

    for i in x:
        if x[i] == False and i == random_empty_gate_open:
            x[i] = None

    print("picked gate ", picked_gate)
    print("random empty gate ", random_empty_gate_open)

    if x[picked_gate]:
        win_or_loose_count += 1

    for i in x:
        print(x[i])

print("count ", win_or_loose_count)
success_rate = win_or_loose_count/1 * 100
print("success rate ", success_rate, "%")
