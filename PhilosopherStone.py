#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 14:47:19 2018

@author: shubham
"""
N = int(input())
A = list(map(int, input().split()))
s = []
flag = 0
q, x = map(int, input().split())
for i in range(q):
    t = input()
    if t == 'Harry':
        b = A.pop(0)
        s.append(b)
        if sum(s) == x:
            print(len(s))
            flag = 1
            break
    else:
        t1 =  s.pop()
        if sum(s) == x:
            print(len(s))
            flag = 1
            break
if flag == 0:
    print('-1')
        
    