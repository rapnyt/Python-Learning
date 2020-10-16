import random
win_or_lose_count_not_changed = 0                                       # Win counter when the gate is not changed
win_or_lose_count_when_changed = 0                                      # Win counter when the gate is changed
tries_range = 1000                                                      # Number of repetitions
numb_gates = 3                                                          # Number of gates in each repetition


for i in range(1,tries_range+1):                                        # For loop for number of repetitions


    x = {}

    for i in range(1,numb_gates+1):                                     # Creation of dictionary with gate numbers and their initial False bool value
        x[i] = False

    winning_gate = random.randint(1,numb_gates)                         # Choosing of the winning gate with random
    x[winning_gate] = True                                              # Altering the dictionary with the winning gate value to True bool value
    picked_gate = random.randint(1,numb_gates)                          # Randomly picking up the gate by the contestant
    unreleaved_gate = winning_gate                                      # Creating an unreleaved gate which the player does not know the content of

    if unreleaved_gate == picked_gate:                                  # The unreleaved gate cannot be the players picked gate, that's why the while loop in conditional
        while unreleaved_gate == picked_gate:
            unreleaved_gate = random.randint(1,numb_gates)
# Not changing the gate scenario
    if x[picked_gate]:
        win_or_lose_count_not_changed += 1
# Changing the gate scenario
    picked_gate = unreleaved_gate
    if x[picked_gate]:
        win_or_lose_count_when_changed += 1

# Final procentage calculations and print commands with the results
win_or_lose_count_not_changed = win_or_lose_count_not_changed /tries_range * 100
win_or_lose_count_when_changed = win_or_lose_count_when_changed /tries_range * 100
print("After", tries_range, "tries.")
print("When gate is not change", win_or_lose_count_not_changed, " %.")
print("When gate is changed", win_or_lose_count_when_changed, " %.")

