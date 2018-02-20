# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 01:07:04 2017

@author: shubham
"""

for _ in range(int(input())):
    n = int(input())
    M = [[0 for i in range(n)] for j in range (n)]
    for i in range(n):
        M[i]=list(map(int, input().split()))
    count = 0
    for p in range(n):
        for q in range(n):
            for i in range(p+1):
                for j in range(q+1):
                    if M[i][j]>M[p][q]:
                        count+=1
    print(count)