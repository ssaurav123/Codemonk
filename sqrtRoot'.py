#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 14:44:34 2018

@author: shubham
"""
for _ in range(int(raw_input())):
    n, m = map(int, raw_input().split())
    flag = 0
    for i in range(m):
        if i**2%m == n:
            flag = 1
            print(i)
            break
    if flag ==0:
        print('-1')
