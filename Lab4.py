# Hieu Ho
# CIS 41B
# Assignment 4

import tkinter as tk
from tkinter import Frame, Message, Label, Button, Radiobutton, messagebox
import multiThreadedLab4 as helper

class Window:
    def __init__(self, root, width = 300, height = 300):
        self.cityList = []
        # Import Object and read the input file
        self.root = root
        self.root.title("Welcome to the weather app")
        self.root.geometry("500x500")
        self.init_page()

    def init_page(self):
        
        self.choose_city_button = tk.Button(text="Choose a city", command=self.popup_city)
        self.choose_city_button.place(relx=0.5, y=15, anchor="c")
        
        self.listbox = tk.Listbox(self.root, height = 20, width = 53)
        self.listbox.place(x=5, y=50)        
        
        self.scrollbar = tk.Scrollbar(root)
        self.scrollbar.pack(side="right", fill="y")
        self.showListBox()

    def showListBox(self):
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)            

    def popup_city(self):
        win = tk.Toplevel()
        win.title("Choose a city")
        win.geometry("250x500")

        weather = helper.Weather(helper.ZIP_CODES)
        cityList = weather.cityList

        # Fix this later
        cityList.sort()

        var = tk.StringVar()
        for city in cityList:
            Radiobutton(win, text = city, value = city, variable = var).pack(anchor = "w")
        
        insert_button = Button(win, text = "Select this city", command=lambda: self.addNewCity(var.get()))
        insert_button.pack()
    
    def addNewCity(self, city):
        weather = helper.Weather(helper.ZIP_CODES)
        sentence = "%s: %d degrees, %s" % (city, weather.weatherInfoDict[city]['temp'], weather.weatherInfoDict[city]['description'])
        self.listbox.insert("end", sentence)


if __name__ == "__main__":
    root = tk.Tk()
    app = Window(root)
    root.mainloop()
        
         
    
        
    
        
        
        