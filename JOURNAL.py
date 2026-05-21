import time
import os
import sys
from datetime import date

actions = ("1. SHOW FILE" , "2. APPEND MESSAGE IN FILE")
def file_show():
    try:
        with open("Journal.txt" , "r") as f:
                return f.read()
    except FileNotFoundError:
           return "DON'T HAVE A MESSAGES"
                
def file_write():
    choose = input("WRITE A MESSAGE: ")
    today = str(date.today())
    with open("Journal.txt" , "a" , encoding="utf-8") as f:
        f.write(f"{today}, {choose}\n")
    return "ADDED😀"    
                
        
print("Hi😀!Do you want a journal?")
choice = input("Yes/No: ")
if choice.lower() == "yes":
    for a in actions:
        print(a)
    action = input("YOU ACTION: ")
    if action == "1":
        w = file_show()
        print(w)
    elif action == "2":
        v = file_write()
        print(v)
    else:
        print("ERROR NUMBER")    
else:
    print("Ok,bye bye👋")
    time.sleep(1.5)
    sys.exit()
    
    
    
    
    