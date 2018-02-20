#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 15:14:52 2018

@author: shubham
"""
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd (b, a%b)
def getCountLattice(x1,y1,x2,y2):
    if x1 == x2:
        return abs(y1-y2)+1
    if y1 == y2:
        return abs(x1-x2)+1
    return gcd(abs(x1-x2), abs(y1-y2))+1
def bsearch(a, x):
    l = 0
    r = len(a)-1
    while l<r:
        mid = (l+r)//2
        if a[mid][0] >= x:
            r = mid
        else:
            l = mid+1
    if a[l][0]>=x:
        return a[l][1]
    else:
        return -1 
s = []
for i in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    t = getCountLattice(x1, y1, x2, y2)
    s.append([t, i+1])
s.sort()
for _ in range(int(input())):
    x = int(input())
    print(bsearch(s,x))
# -26 37 -80 53
#-15420 -74219 -16168 -79489
#12503 23456 14971 13990   
# 