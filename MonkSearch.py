#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 13:22:23 2018

@author: shubham
"""
def Low(a, l, r, x):
    while l<r:
        mid = (l+r)//2
        if a[mid] >= x:
            r = mid
        else:
            l = mid+1
    if a[l]>=x:
        return l
    else:
        return -1
def High(a, l, r, x):
    while l<r:
        mid = (l+r)//2
        if a[mid] > x:
            r = mid
        else:
            l = mid+1
    if a[l]> x:
        return l
    else:
        return -1
    
n = int(input())
A = list(map(int, input().split()))
A.sort()
Q = int(input())
for _ in range(Q):
    p, q = map(int, input().split())   
    if p == 0:
        t = Low(A, 0, n-1, q)
        if t>=0:
            print(n-t)
        else:
            print('0')
    else:
        t = High(A, 0, n-1, q)
        if t>=0:
            print(n-t)
        else:
            print('0')