import random
import time
from termcolor import colored
from colorama import init, Fore, Back, Style
init()
print(Fore.RED + 'Red')
print(Fore.GREEN + 'Green')
print(Fore.BLUE + 'Blue')
print(Style.RESET_ALL)
elements_list=["a"," ","b","c","d","e","f","g","h"," ","o","p","q","r"," ","s","t","u"," ","x","w","y","z","!","?","@"]

max_width=50

while True:
    current_line_string=""
    for element in range (0,max_width):
        current_line_string=current_line_string+(elements_list[random.randint(0,(len(elements_list)-1))])+" "
    color_line=colored(current_line_string,'green')
    print (color_line)
    time.sleep(0.04)