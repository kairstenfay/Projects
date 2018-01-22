#!/bin/python3

import sys

arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

def hourglass(arr):
    i=0
    max= -1*sys.maxsize ## smallest possible integer
    while i+2 <= 5:
        j=0
        while j+2 <= 5:
            top = arr[i][j]+arr[i][j+1]+arr[i][j+2]
            bottom = arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            middle = arr[i+1][j+1]
            total = top+bottom+middle
            if total > max:
                max = total
            j += 1
        i += 1
    print(max)
    return

hourglass(arr)