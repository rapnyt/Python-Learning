'''

Common exceptions:
ImportError: an import fails;
IndexError: a list is indexed with an out-of-range number;
NameError: an unknown variable is used;
SyntaxError: the code can't be parsed properly;
TypeError: a function is called on a value of an inappropriate type;
ValueError: a function is called on a value of the correct type, but with an inappropriate value.

'''

try:
    print("sfkjhsd")
except NameError:
    print("\nThere is no such a variable called ...")
except (ValueError, TypeError):
    print("This will run in case of value or type error")
except:
    print("This will run if any error occurs")
finally:
    print("This code will run no matter what even if there is uncaught exception")

if False:
    raise ValueError
    assert 2 == 4  # This is sanity check

temp = 16
assert (temp > 0), "Colder than absolute zero"

myfile = open("filename.txt")

'''
You can specify the mode used to open a file by applying a second argument to the open function.
Sending "r" means open in read mode, which is the default.
Sending "w" means write mode, for rewriting the contents of a file.
Sending "a" means append mode, for adding new content to the end of the file.

Adding "b" to a mode opens it in binary mode, which is used for non-text files (such as image and sound files).
'''

myfile = open("filename.txt","w")
print("I like learning coding in python")
myfile.close()
