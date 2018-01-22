#!/bin/python3

import sys


n = int(input().strip())

binary = ""

while n >= 1:
    if n > 1:
        rem = n % 2
        n = (n - rem)/2
        n = int(n)
        rem = int(rem)
        binary += str(rem)
    elif n==1:
        binary += "1"
        break

binary = binary[::-1] 

        
max = 0
conseq = 0
for i in range(0, len(binary)):
    if binary[i] == "1":
        conseq += 1
        if conseq > max:
            max = conseq
    elif binary[i] == "0":
        conseq = 0

print(max)
