#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 22:46:31 2018

@author: shubham
"""

N = int(input())
s =[]
for i in range(N):
    s.append(input())
for i in range(len(s)):
    count = 0
    for j in range(i):
        if s[j]<s[i]:
            count+=1
    print(count)