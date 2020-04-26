'''
This is my code with all necessary commands, def, arguments, parameters to have everything sorted out
'''

print("Hello world")
print("First string" + ", " + "second string")  # print with strings
my_age = "32"

my_desired_age = int(my_age) - 10  # unit conversion

my_boolean = True
print(my_boolean)  # booleans
print(2 == 3)

if my_desired_age < int(my_age):
    print("You sick bastard")
else:  # conditionals
    print("You'd wish")

if "fuck" == "cunt":
    print("luck")
elif "fuck" == "slack":
    print("damn")
elif True:
    print("yay")

my_age = int(my_age)

while my_desired_age < my_age:  # while loop
    print(my_desired_age)
    my_desired_age += 1

i = 0

while True:  # infinite while loop with break point and ommittments
    i += 1
    if i % 2 == 0:
        continue
    print(i)
    if i > 51:
        break

my_age == my_desired_age or my_age == my_desired_age and my_boolean != my_desired_age  # operators

words = ["hello", "fuck","no",[1,2,3]] # lists
words[0] = "lalaa"
print(words[0],words[3][1])
print(words[3]*5)
print("fuck" in words)
print(not "nosdf" in words)
empty_list = []
empty_list.append(4)
print(len(empty_list))
empty_list.insert(0,"to be")
print(empty_list)
print(empty_list.index("to be"))

numbers = list(range(10,20,3)) # range
print(numbers)

for skfhdklfh in words: # for loops
    print(str(skfhdklfh) + "!")
for j in range(5):
    print("fuck ")

def my_dick():
    print("Its so big")
my_dick()