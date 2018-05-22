print('GovTuner Logo')

import math
print(math.ceil(79.6))

import os
print(os.getcwd())

#f is a variable where we declare the file as well as open it, for the usage of this file in future instances it can be called via 'f.function' w=write, a=append, r=read...
f = open("testfile.txt", "w+") 
f.write("This is a testfile")
f.close()

g = open("value.txt", "w+")
#Note the range syntax, write needs the argument as 'str' , but the built-in fuction 'str' can take 'int' arguments and perform arithmetic operations on them as shown, write can only take 1 argument so special characters such as carriage returns should follow on the next line to have the desired effect
for i in range(0, 10):
   g.write(str(int(i)*int(1267)))
   g.write("\n")

#To read the contents of a file and store it in a variable the 'with' keyword is important, rest of the code is self-explanatory, observe the 'with' usage and syntax.
with open("testfile.txt", "r") as contents:
   s = contents.read()
   print(s)


print("Yes", s[0])
