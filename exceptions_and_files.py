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
    print(sfkjhsd)
except NameError:
    print("\nThere is no such a variable called ...")
except (ValueError,TypeError):
    print("kakaka")
except:
    print("jfdsjkfhds")