#!/usr/bin/python3
# Alex Jordan
#2/10/2020

'''GUI for Media Library'''

import pickle
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

TITLE_FONT = ("Times New Roman", 24)
BUTTON_FONT = ("Arial", 15)

class MainMenu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_title = tk.Label(text = "Game Library", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        self.btn_add = tk.Button(text = "Add", font = BUTTON_FONT)
        self.btn_add.grid(row = 1, column = 0)       
        
class SearchMenu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_title = tk.Label(text = "Search", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        
        self.lbl_search = tk.Label(text = "Search by: ", font = BUTTON_FONT)
        self.lbl_search.grid(row = 1, column = 0, sticky = "news")
        
        self.lbl_search2 = tk.Label(text = "Search for: ", font = BUTTON_FONT)
        self.lbl_search2.grid(row = 3, column = 0, sticky = "news")        
        
        self.ent_box1 = tk.Entry()
        self.ent_box1.grid(row = 2, column = 0)
        
        self.ent_box2 = tk.Entry()
        self.ent_box2.grid(row = 4, column = 0)
        
        
        
        self.scrolled_text = ScrolledText()
        self.scrolled_text.grid(row = 5, column = 0, columnspan = 3)        
        
        
            
         
        
         
        
        
        

##MAIN
if __name__ == "__main__":
    datafile = open("game_lib.pickle", "rb")
    games = pickle.load(datafile)
    datafile.close()    
    root = tk.Tk()
    root.title("Game Lib")
    root.geometry("500x500")
    
    main_menu = MainMenu()
    main_menu.grid(row = 0, column = 0)
    
    search_menu = SearchMenu()
    search_menu.grid(row = 0, column = 0)
    
    root.grid_rowconfigure(0, weight = 1)
    root.grid_columnconfigure(0, weight = 1)
    
    root.mainloop()
    
    