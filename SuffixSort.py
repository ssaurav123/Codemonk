#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 22:22:50 2018

@author: shubham
"""
s, k = input().split()
K = int(k)
t = []
for i in range(len(s)):
    t.append(s[i:])
t.sort()
print(t[K-1])