# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 00:44:16 2017

@author: shubham
"""
for _ in range(int(input())):
    s = input()
    flag = 0
    for i in range(0,len(s)):
        if s[i] != s[len(s)-1-i]:
            flag = 1
            print('NO')
            break
    if flag == 0:
        if len(s)%2 == 0:
            print('YES', 'EVEN')
        else:
            print('YES','ODD')
            