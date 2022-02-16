#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import webbrowser
import tkinter as tk
from tkinter import filedialog
from tkinter import Tk, filedialog

def create_folder():
    number = int(number_of_folder_input.get())
    number += 1
    name = name_of_folder_input.get()
    root = Tk() # pointing root to Tk() to use it as Tk() in program.
    root.withdraw() # Hides small tkinter window.
    root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.

    destination_path = filedialog.askdirectory(title="select folder")
    for folder in range(1,number):
        folder_number=(f"%s{folder}")%(name)
        try:
            os.mkdir(os.path.join(destination_path,folder_number))
            print(f"Creating...Folder{folder_number}")
        except FileExistsError:
            print(f"{folder_number} Exist")
    webbrowser.open(destination_path)
    result_label.configure(text = "Complete creating folder")
    

window = tk.Tk()
window.title("Create Folder")
window.minsize(width = 100,height = 100)

#choose number of folder
title_label = tk.Label(master=window, text = "how many folder do you want to create?")
title_label.pack()
number_of_folder_input = tk.Entry(master=window)
number_of_folder_input.pack()

#name of folder
title_label = tk.Label(master=window, text = "what is your folder name? "+"(Optional)")
title_label.pack()
name_of_folder_input = tk.Entry(master=window)#
name_of_folder_input.pack()

#choose destination
title_label = tk.Label(master=window, text = "Where do you want to create folder ?")
title_label.pack()
choose_destination_button = tk.Button(master=window,text="choose destination",command=create_folder)
choose_destination_button.pack()

#checking
result_label = tk.Label(master=window)
result_label.pack()

window.mainloop()
        
        
    
   


# In[ ]:




