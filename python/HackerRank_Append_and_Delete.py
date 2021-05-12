#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    i=0
    j=0
    while 1:
        if s[i]==t[i]: 
            if i==len(s)-1: break
            elif i==len(t)-1: break
            i+=1
        else : break 
    if len(s)+len(t)<k:return 'Yes'
    elif len(s)-i-1+(len(t)-i-1)<k and abs(len(s)-i-2+len(t)-i)%2==k%2: return 'Yes'
    elif len(s)-i-1+(len(t)-i-1)<k and len(s)==len(t): return 'Yes'
    else:return 'No'
        
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
