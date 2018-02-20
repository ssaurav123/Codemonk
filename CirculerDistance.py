#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 00:02:08 2018

@author: shubham
"""
def Low(a, l, r, x):
    while l<r:
        mid = (l+r)//2
        if a[mid] > x:
            r = mid
        else:
            l = mid+1
    if a[l]>x:
        return l
    else:
        return -1

        
N = int(input())
s = []
for i in range(N):
    s.append(list(map(int, input().split())))
for i in range(N):
    s[i] = (s[i][0]**2 + s[i][1]**2)**(1/2)
s.sort()
q = int(input())
for _ in range(q):
    r = int(input())
    
    t = Low(s, 0, N-1, r)
    if t == -1:
        print(N)
    else:
        print(t)
    
            