#%%
"""
GUI practice (A text editor.)
"""
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

#Definition of events
#Open the txt file
def open_file():
    filepath = askopenfilename(
        filetypes = [("Text Files", "*.txt"),
                     ("All Files", "*.*")]
        )
    
    if not filepath:
        return
    
    txt_edit.delete("1.0", tk.END) 
    #tk.END is a command about reading to the end.
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    
    #The with statement itself ensures proper acquisition
    #and release of resources. In this case, input_file.close
    #is not needed.
    window.title(f"Simple Text Editor - {filepath}")

#Save the txt file
def save_file():
    filepath = asksaveasfilename(
        defaultextension = "txt",
        filetypes = [("Text Files", "*.txt"),
                     ("All Files", "*.*")]
        )
    
    if not filepath:
        return
    
    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
        window.title("Simple Text Editor - {filepath}")
        

#Window 
window = tk.Tk()
window.title("Simple Text Editor")

window.rowconfigure(0, minsize = 800, weight = 1)
window.columnconfigure(1, minsize = 800, weight = 1)

#The widgets' layouts 

#Text bar
txt_edit = tk.Text(master = window)

fr_btn = tk.Frame(master = window)

#Open button
btn_op = tk.Button(master = fr_btn, text = "Open", command = open_file)
btn_op.grid(row = 0, column = 0, sticky = "ew",
            padx = 5, pady = 5)

#Save button
btn_sa = tk.Button(master = fr_btn, text = "Save as ...", command = save_file)
btn_sa.grid(row = 1, column = 0, sticky = "ew",
            padx = 5)

fr_btn.grid(row = 0, column = 0, sticky = "ns")
txt_edit.grid(row = 0, column = 1, sticky = "nsew")


window.mainloop()





