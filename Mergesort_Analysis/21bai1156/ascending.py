#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 21:24:46 2022

@author: janaki
"""
n=50000
fp = open("ascending_50000.txt","w")
fp.write(str(n)+" ")  
for i in range(1,n):
    fp.write(str(i)+" ")  
fp.write(str(n))
fp.close()