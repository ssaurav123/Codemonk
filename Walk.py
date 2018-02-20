#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 13:11:20 2018

@author: shubham
"""
for _ in range(int(input())):  
    s = input()
    t = s.lower()
    count = t.count('a') + t.count('e') + t.count('i') + t.count('o') + t.count('u')
    print(count)