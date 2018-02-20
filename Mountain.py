#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 02:20:57 2018

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
N, Q = map(int, input().split())
s = []
t = []
for i in range(N):
    l, r = map(int, input().split())
    s.append(r)
    t.append(r-l+1)
for i in range(1, N):
    t[i] = t[i-1] + t[i]
for i in range(Q):
    x = int(input())
    u = Low(t, 0, N-1, x)
    v = t[u] - x
    print(s[u] - v)