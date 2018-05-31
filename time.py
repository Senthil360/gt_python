#This file will be intergrated into gt.py
#The objective of this code is to obtain time_in_state of the CPU and adjust target loads accordingly with the help of an algorithm

import math #for future functions

def takeSecond(elem):
   return elem[1]

a = open("time_in_state", "r")
b = a.read()
a.close()

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

d = (b.splitlines())

e=[]
f=[]

for i in d:
   e.append(i.split(' ')[0])
   f.append(i.split(' ')[1])

g=[]
c = file_len("time_in_state")
count=0

while count < c:
   g.append([])
   g[count].append(int(e[count]))
   g[count].append(int(f[count]))
   count = count+1

h = sorted(g, key=takeSecond)


   
   
