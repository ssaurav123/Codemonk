#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 02:41:09 2018

@author: shubham
"""
def merge(arr, l, m, r,K):
    n1 = m - l + 1
    n2 = r- m
 
    
    L = [0] * (n1)
    R = [0] * (n2)
 
   
    for i in range(0 , n1):
        L[i] = arr[l + i]
 
    for j in range(0 , n2):
        R[j] = arr[m + 1 + j]
 
    
    i = 0     
    j = 0     
    k = l     
 
    while i < n1 and j < n2 :
        if L[i]%K <= R[j]%K:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
   
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 

def mergeSort(arr,l,r,K):
    if l < r:
 
        
        m = (l+(r-1))//2
 
        
        mergeSort(arr, l, m,K)
        mergeSort(arr, m+1, r, K)
        merge(arr, l, m, r, K)
N, k = map(int, input().split())
a = list(map(int, input().split()))
mergeSort(a,0,len(a)-1,k) 
print(*a)