# Hieu Ho
# CIS 41B
# Assignment 4

import tkinter as tk
from tkinter import Frame, Message, Label, Button, Radiobutton, messagebox

cityDict={}

class Window:
    def __init__(self, root, width = 300, height = 300):
        # Import Object and read the input file
        self.root = root
        self.root.title("Welcome to the weather app")
        self.root.geometry("500x500")
        self.init_page()

    def init_page(self):
        
        self.chooseaCity_button = tk.Button(text="Choose a city", command=popup_chooseaCity)
        self.chooseaCity_button.place(relx=0.5, y=0, anchor="c")
        
        self.listbox = tk.Listbox(self.root, height = 20, width = 53)
        self.listbox.place(x=5, y=50)        
        
        self.scrollbar = tk.Scrollbar(root)
        self.scrollbar.pack(side="right", fill="y") 
        self.showListBox()
        
    def showListBox(self):
        if city in cityDict:
            for city in cityDict.fetchall():
                    self.listbox.insert("end", str(city[0]))
    
    
    self.listbox.config(yscrollcommand=self.scrollbar.set)
    self.scrollbar.config(command=self.listbox.yview)            
    self.root.after(100, self.showListBox)    
      
      
def popup_chooseaCity():
    
    win=tk.Toplevel()
    win.title("Choose a city")
    win.geometry("250x500")
    
    var = tk.StringVar()
    for city in cityList.fetchall():
        Radiobutton(win, text = genre[0], value = str(genre[1]), variable = var).pack(anchor = "w")    
    
    plot_button = Button(win, text = "Ok", command = lambda: get_list_city(win, var.get()))
    plot_button.pack()

def get_list_city(win,value):
    
    
    
    


if __name__ == "__main__":
    root = tk.Tk()
    app = Window(root)
    root.mainloop()
        
         
    
        
    
        
        
        