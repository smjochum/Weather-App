# Hieu Ho
# CIS 41B
# Assignment 4

import tkinter as tk
from tkinter import Frame, Button, Radiobutton, messagebox, filedialog, Scrollbar
import multiThreadedLab4 as helper
import os

DEBUG_VALUE = False

class Window:
    def __init__(self, root, width = 300, height = 300):
        # Import Object and read the input file
        self.root = root
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.title("Welcome to the weather app")
        self.root.geometry("500x500")
        self.init_page()
        #self.update()

    def init_page(self):

        # ``````````````City Button```````````````````````````````````````````````
        self.choose_city_button = tk.Button(text="Choose a city", command=self.popup_city)
        self.choose_city_button.place(relx=0.5, y=15, anchor="c")
        

        # ````````````````Scrollbar & Listbox``````````````````````````````````````````
        self.scrollbar = Scrollbar(self.root)
        self.scrollbar.pack(side = "right", fill = "y")

        self.listbox = tk.Listbox(self.root, height = 20, width = 53, yscrollcommand = self.scrollbar.set)
        self.listbox.place(x=5, y=50)
        self.scrollbar.config( command = self.listbox.yview)      


    def popup_city(self):
        win = tk.Toplevel()
        win.title("Choose a city")
        win.geometry("250x400")

        weather = helper.Weather(debug=DEBUG_VALUE)
        cityList = weather.cityList
        cityList.sort()

        var = tk.StringVar()
        var.set(cityList[0])

        for city in cityList:
            Radiobutton(win, text = city, value = city, variable = var).pack(anchor = "w")
        
        insert_button = Button(win, text = "Select this city", command=lambda: self.addNewCity(var.get()))
        insert_button.pack()
    
    def addNewCity(self, city):
        weather = helper.Weather(debug=DEBUG_VALUE)
        sentence = "%s: %d degrees, %s" % (city, weather.weatherInfoDict[city]['temp'], weather.weatherInfoDict[city]['description'])
        self.listbox.insert("end", sentence)
    
    def on_closing(self):
        if (self.listbox.size() > 0) and messagebox.askokcancel("Save", "Do you want to save your file?"):
            dir = filedialog.askdirectory(initialdir=os.getcwd())
            if dir != "":
                filename = dir + "/weather.txt"
                messagebox.showinfo("save", "File weather.txt will be save in %s" % dir)
                with open(filename, 'w') as fout:
                    fout.write('\n'.join(self.listbox.get(0, "end")))
                    fout.close()            

        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = Window(root)
    root.mainloop()