morty = None #absense of value, equals False as Boolean
rick = 0
print(bool(morty))
print(bool(rick))

def funct(): #no return so returns None
    print("hi")

print(funct())

ages = { #this is a dictionary, keys can be only immutable
    "Dave": 24,
    "Mike": 30,
    "Oli": 55 }

print(ages["Dave"])

names = {} #a empty dictionary

print("BMW" in ages)
print(ages.get("bmw"))

list_s = [2,3,4,5,6]
tuple_s = (2,3,4,5,6) #tuple example or..
tuple_m = 2,3,4,5,6 #without paranthesis
print(list_s[2:4:1]) #list slices
print(list_s[::2])
cubes = [i**3 for i in range(0,23,2) if i % 3 == 0] #making list with simple mathematical rule
print(cubes)

msg = "Message to our user: {0} {1}            {2}".format(list_s[4],list_s[1],list_s[3]) #string formatting
print(msg)

print("*".join(str(list_s[1:4]))) #useful functions
print(msg.replace("Message","Me"))
print(msg.startswith("Me"))
print(msg.endswith("5"))
print("This is string".upper())
print("This is string".lower())
print("skdlfjlkdjfdslkfsdjflk, sdfljdslfksdl, sdlfkjs, dfjjf, 22,2,4,4,3,3".split(","))
print(min(list_s))
print(max(list_s))
print(abs(list_s[3]))
print(sum(list_s))
if all(i > 0 for i in list_s):
    print("hahahaha")

if any(i < 0 for i in list_s):
    print("hahahaha")

for sjfldsjflsk in enumerate(list_s):
    print(sjfldsjflsk)


def count_char(text,char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count


filename = input("Enter full filename without extension: ")
filename += ".txt"
try:
    with open(filename) as f:
        text = f.read()
        print(text)
        alphabet_string = "abcdefghijklopqrstuvwxyz"
        for char in alphabet_string:
            percentage = 100 * count_char(text, char) / len(text)
            print("{0} {1}%".format(char,round(percentage,5)))
    f.close()
except:
    print("There is no such file in the directory")


'''
The following are some immutable objects:
int
float
decimal
complex
bool
string
tuple
range
frozenset
bytes

The following are some mutable objects:
list
dict
set
bytearray
'''