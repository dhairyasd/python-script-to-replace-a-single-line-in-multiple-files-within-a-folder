# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:34:17 2020

@author: Dhairya's Laptop
"""

import glob
import os
files = glob.glob("config/*.ovpn")
for x in range(0,len(files)):
    f = open(files[x],'r')
    t = open("temp.txt",'w')
    for line in f:
        if "auth-user-pass" in line:
            t.write("auth-user-pass pass.txt")
        else:
            t.write(line)
    f.close()
    t.close()
    os.remove(files[x])
    os.rename("temp.txt",files[x])
    print("File no ",x+1,"'s replacement done")