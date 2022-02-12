# -*- coding: utf-8 -*-
# user/computer know what is the encoding system
"""
Created on Fri Jan  8 16:32:24 2021
@author: zaza/HW

Goal:
    Basic demonstration for beginner
    
Description:
    xxx
    
log:
    20200112 Revised from HWs script

^^^ Important Notes should be add in this long comment section.
0. What is the meaning of the 
1. Usage of each Blocks on GUI
2. Usage of short and long comment 
3. Hello world (shift-Enter)
"""

#%% Basic I/O; error; line-by-line execution
print("Hello world!") #print hello on the console

data = input("type anything:") #variable named data
print(data) #printout data
print("what you type is:" + data)

print(data1) #oh! error!
del data #I don't want data anymore in memory (less use)

#%% Build-in data type
# a=1
# b=0.1
# c=1+1j
a, b, c, = 1, 0.1, 1+1j # number: integer, float, complex
print(a,b,c)
print(type(a), type(b), type(c))
print(int(b), float(a)) #change type

s1, s2 = "1", "Hello" # String
print(s1, s2)
print(type(s1), type(s2))

list1 = [1, 2, 3] # list with nuber
list2 = ["1", 1, "hi"] # list with mixed element
print(list1)
print(list2[0], list2[1], list2[2]) #print individually
#%% Conditional Judgment and if/else
"""
Boolean judgment(==, >=, <=, !=)

Examples:
1==1
1==2
1>2
1<=2
1!=2
"""
#judge if the number is larger/smaller/equal to zero from the input
userInput = input("enter a real number: ")
data = float(userInput)
if data>0:
    print( data, " is greater than 0.")
elif data<0:
    print(data, " is smaller than 0.")
elif data>10 and data<20:
    print(data, " is in the range (10, 20)")
else:
    print(data, " is equal to 0.")
    
# Advence example: only can input number    
# try:
#     data = float(userInput)
#     if data>0:
#         print( data, " is greater than 0.")
#     elif data<0:
#         print(data, " is smaller than 0.")
#     else:
#         print(data, " is equal to 0.")
# except ValueError:
#     print("Not a digit!")

#%% for loop
# Example: Number counting
ans = 0 # set "ans" variable as 0
for i in range(10):
    ans  = ans + i
    print(ans)

# fast way
# sum(range(10))

# Example: nest loop
# for i in range(10):
#     for j in range(10):
#         print(i*j)

# Example: using list
# list10 = ['10', '01', '100', '101']
# for keys in list10:
#     print(keys)

# Example: index and keys
# list10 = ['10', '01', '100', '101']
# for index, keys in enumerate(list10):
#     print(keys, index)
    
    
#%% array and nested loop
#include the package "numby"
# you can name like this: import numpy as whyiamhere
# That increases the diffcult to read
import numpy as np  
# comparing with two similar list
# aa = range(2, 10, 2) # not an array
# bb = np.arange(2, 10, 2) #array with [2, 4, 6, 8]

nn = np.zeros([9,9]) #set zeros [9x9]
# nn.shape #check the shape

start, end = 1, 10
#nest loop itself
for i in np.arange(start, end):
    for j in np.arange(start, end):
        nn[i-1, j-1]=i*j #give every value to the 2D array
        
#while loop


#%% function and plot
# set the inline to QT5
#define a function named "func_1"
def func_1(arr):
    ans = np.exp(arr) 
    # what actually the upper line did
    # ans=np.empty(len(arr))
    # for i, key in enumerate(arr):
    #     ans[i]=key
    return ans

#frequently used plot package
import matplotlib.pyplot as plt 

x = np.linspace(0, 1, 100) #create an array with 100 size from 0 to 1
y = func_1(x) #call the function func_1 and output the result to y
plt.plot(x, y) # plot x to x; y to y.

#%% Appendix
'''
Python tutorial
Official site
https://docs.python.org/3/tutorial/index.html
RIP tutorial
https://riptutorial.com/python
Numpy tutorial 
https://numpy.org/doc/stable/user/quickstart.html
matplotlib
https://matplotlib.org/tutorials/index.html

Book: 
    Essential Python for the physicist (Strongly recommend!)
    
Additional informaiton (increasing building speed)
- Common short-cut (F9/Shift-Enter/F5)
- Magic commands (%clear; %reset; %timeit)



Some commands:
    - Google documents/online resources.
    - Calculate fast is not the fastest way to finish.
    - Do comments.
    - Easy read name for variable.
    - Do not build the wheel again. (Unless you are practicing)
    
'''


