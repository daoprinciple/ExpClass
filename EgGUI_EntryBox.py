# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 15:40:15 2021
Goal:
	Example for showing the basic I/O for GUI application

@author: zaza
"""

import tkinter as tk 

#you should better put the definition immidiately after the definiton.
def getSquareRoot ():  
    x1 = entry1.get()
    
    label1 = tk.Label(root, text= float(x1)**0.5)
    canvas1.create_window(200, 230, window=label1)

root= tk.Tk()

# create canvas
canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

# input a number
entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

button1 = tk.Button(text='Get the Square Root', command=getSquareRoot)
canvas1.create_window(200, 180, window=button1)


root.mainloop()
