#!/bin/python3

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
#arr = arr.reverse() # hmm? 

i = n-1
answer = ""
while i>=0:
    answer += str(arr[i]) + " "
    i -= 1
print(answer)
