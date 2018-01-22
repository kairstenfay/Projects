# Exceptions
#!/bin/python3

import sys


S = input().strip()

def stringToInt(string):
    try:
        I = int(S)
        print(I)
    except:
        print("Bad String")
        
stringToInt(S)