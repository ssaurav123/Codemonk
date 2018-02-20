# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 19:15:25 2018

@author: shubham
"""
for _ in range (int(input())):
    N, K = map(int, input().split())
    s = list(map(int, input().split()))
    t = []
    for i in range(N-K%N, N):
        t.append(s[i])
    for i in range(N-K%N):
        t.append(s[i])
    print(*t)
