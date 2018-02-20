#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 13:19:17 2018

@author: shubham
"""

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)
d1 = 1
x = 0
y = 0
def ExtendedEuclid(a, b):
    global d1
    global x
    global y
    if b==0:
        d1 = a
        x =1
        y =0    
    else:
        ExtendedEuclid(b, a%b)
        temp = x
        x =y
        y = (temp-(a//b)*y)
        

def modInverse(a, m):
    ExtendedEuclid(a, m)
    return ((x%m)+m)%m
for _ in range(int(input())):
    a, b, d = map(int, input().split())
    
    if d==0:
        print('1')
        continue
    else:
        g = gcd(a,b)
        if d%g !=0:
            print("0")
            continue
        else:
            a//=g
            b//=g
            d//=g
            m = modInverse(b, a)
            y1 = ((d%a) * m)%a
            if d<b*y1:
                print("0")
                continue
            else:
                n = (d/b-y1)/a
                print(int(n)+1)
        
        