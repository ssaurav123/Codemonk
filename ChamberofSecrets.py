#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 13:43:40 2018

@author: shubham
"""
n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in range(len(a)):
    a[i] = [a[i], i+1]
for l in range(x):
    c = []
    count = 0
    for r in range(x):   
        if len(a)>0:
            c.append(a.pop(0))
    max = [-1]
    for i in range(len(c)):
        if c[i][0]>max[0]:
            max = c[i]
    for i in range(len(c)):
        if c[i][0]>0:
            if c[i][0] != max[0] or count == 1:
                a.append([c[i][0]-1, c[i][1]])
            else:
                count = 1
        elif c[i][0] == 0 and c[i][1] != max[1]:
            a.append(c[i]) 
    if max[0] != -1:
        print(max[1], end = ' ' )
    
