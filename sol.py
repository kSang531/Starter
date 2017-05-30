#!/usr/bin/python
""" Simple pattern generator """
n = int(raw_input('Enter the sequence length:'))
if n <= 0: raise Exception('Valid non-zero positive integer should be entered.')
if n >= 26: raise Exception("Number greater than twenty-five cannot be entered.')
for i in range(n, -1, -1):
    for j in range(i):
        print chr(ord('A') + j),
    for s in range(n-i): print ' ',
    for s in range(n-i-1): print ' ',
    if i == n: 
        for k in range(i-2, -1, -1): 
            print chr(ord('A') + k),
    else:
        for k in range(i-1, -1, -1):
            print chr(ord('A') + k),
    print
    
