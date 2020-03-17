# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:34:17 2020

@author: Dhairya's Laptop
"""
PATH_OF_CONFIG = "C:/Program Files/OpenVPN"
import glob
import os
files = glob.glob(PATH_OF_CONFIG+"/config/*.ovpn")
for x in range(0,len(files)):
    f = open(files[x],'r')
    t = open("temp.txt",'w')
    flag = 0
    for line in f:
        if "block-outside-dns" in line:
            flag = 1
            break
    f.seek(0)
    for line in f:
        if "auth-user-pass" in line:
            t.write("auth-user-pass pass.txt\n")
            if flag == 0: 
                t.write("block-outside-dns\n")
        else:
            t.write(line)
    f.close()
    t.close()
    os.remove(files[x])
    os.rename("temp.txt",files[x])
    print("File no ",x+1,"'s replacement done")