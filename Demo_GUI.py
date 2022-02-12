# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 22:19:04 2021
Goal:
    Demonstration of building the GUI function

Reference:
    https://www.delftstack.com/zh-tw/tutorial/tkinter-tutorial/
    https://realpython.com/python-gui-tkinter/

@author: zaza
"""

# main package for GUI interface
import tkinter as tk #only import once in this script
# import tkinter as * <- not a good habit!

#%% Frequently used objects
window = tk.Tk() #create the window
# properties of this object "window"
window.title('Hello') #window named "Hello"
window.geometry('500x500') #size of the window

#Label 
label_1 = tk.Label(text = 'hello world', bg='yellow')
label_1.pack(ipadx=30, padx=20, fill='x') #layout setting; default
# padx x axis of pad
# ipadx x axis of pad "inside the object"

#Button
button = tk.Button(
            text = "Click",
            width = 25,
            height = 5,
            bg = "black",
            fg = "white",
            )
button.pack() #default setting


entry = tk.Entry() #write sth.
# entry.pack(side='bottom', expend='yes')
entry.pack(side='bottom')

window.mainloop() #Start the window and do while loop
#%% window layout (put object to the correct position)
#pack(); grid(); place()
#%% Bottom control example with grid layout
def func_increase():
    '''increasing number function

    '''
    value = int(lbl_value['text']) # the object lbl_value cha
    lbl_value["text"] = f"{value + 1}" # 
    

window = tk.Tk() #simple window

#layout configuration
window.rowconfigure(0, minsize = 50, weight = 1) #1 row
window.columnconfigure([0, 1, 2], minsize = 50, weight = 1) # 3 column

#botton on right for +1
btn_dec = tk.Button(master = window, text = "+", command = func_increase)
btn_dec.grid(row = 0, column = 0, sticky = "nsew") #fill the grid

#show the result by label
lbl_value = tk.Label(master = window, text = "0")
lbl_value.grid(row = 0, column = 1)

window.mainloop()

#%% Canvas (Draw sth.)
# window settings
window = tk.Tk()
window.title('Canvas') #window named "Hello"
window.geometry('500x500') #size of the window

#create an object "canvas"
canvas = tk.Canvas(window, width=200, height=200, bg='white')
canvas.pack(padx=20, pady=20)

# create line and rectangle
canvas.create_line(10, 10, 200, 200) 
canvas.create_rectangle(10, 10, 20, 20, fill='black')

tk.mainloop()
