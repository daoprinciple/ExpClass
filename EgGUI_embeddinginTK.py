# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 17:16:36 2021
Embedding in Tk
@author: zaza

Ref: https://matplotlib.org/3.1.0/gallery/user_interfaces/embedding_in_tk_sgskip.html
"""

import tkinter as tk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np


root = tk.Tk()
root.wm_title("Embedding in Tk")

#figure plot; set as the original method.
fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, .2, .01)
ax1 = fig.add_subplot(111)
ax1.plot(t, 2 * np.sin(2 * np.pi * t))
ax1.grid()
ax1.tick_params(direction='in', length=6, width=2, colors='r',
               grid_color='r', grid_alpha=0.5)
ax1.set_xlabel("x(n)")
ax1.set_ylabel("f(x)")

# A tk.DrawingArea.
canvas = FigureCanvasTkAgg(fig, master=root)  
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)

canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button = tk.Button(master=root, text="Quit", command=_quit)
button.pack(side=tk.BOTTOM)

tk.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.
