#!/bin/python3

import sys


n = int(input().strip())

for i in range(1,11):
        result = n*i
        print("{} x {} = {}".format(n,i,result))