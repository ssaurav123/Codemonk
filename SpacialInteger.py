#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 20:39:02 2018

@author: shubham
"""
def bsearch(prefix, n, k):
    ans , l, r = -1, 1, n
    
    while l<=r:
        flag = 0
        mid = (l+r)//2
        for i in range(mid, n+1):
            if prefix[i]-prefix[i-mid] >k:
                flag = 1
                break
        if flag == 0:
            l = mid+1
            ans = mid
            
        else:
            r = mid-1
    return ans
            
N, X = map(int,input().split())
A = list(map(int, input().split()))
count = 0
flag = 0
prefix = [0] *(N+1)
for i in range(1, N+1):
    prefix[i] = prefix[i-1] + A[i-1]
print(bsearch(prefix, N, X))