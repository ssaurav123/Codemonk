# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 18:50:44 2018

@author: shubham
"""
s = input()
count = 0
t = 0
for i in range(len(s)):
    if s[i] == 'a'or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
        count += 1
        if count > t:
            t = count
    else:
        count = 0
print(t)
    