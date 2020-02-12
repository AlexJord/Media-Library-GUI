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
        
        options = ["one", "two"]
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options[0])
        self.ent_box1 = tk.OptionMenu(self, self.tkvar, *options)
        self.ent_box1.grid(row = 2, column = 0, sticky = "news")        
         
        self.ent_box2 = tk.Entry()
        self.ent_box2.grid(row = 4, column = 0, sticky = "news")     
        
        btn_filters = BTN_Filters()
        btn_filters.grid(row = 1, column = 1)        
        
        self.scrolled_text = ScrolledText()
        self.scrolled_text.grid(row = 5, column = 0, columnspan = 3)    
        
        
class BTN_Filters(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        
        self.title = tk.Checkbutton(self, text = "Title")
        self.title.grid(row = 0, column = 0, sticky = "news")
        
        self.genre = tk.Checkbutton(self, text = "Genre")
        self.genre.grid(row = 1, column = 0, sticky = "news")
        
        self.developer = tk.Checkbutton(self, text = "Developer") 
        self.developer.grid(row = 2, column = 0, sticky = "news")   
        
        self.publisher = tk.Checkbutton(self, text = "Publisher")
        self.publisher.grid(row = 3, column = 0, sticky = "news")     
        
        self.system = tk.Checkbutton(self, text = "System")
        self.system.grid(row = 0, column = 1, sticky = "news")  
        
        self.release = tk.Checkbutton(self, text = "Release Date")
        self.release.grid(row = 1, column = 1, sticky = "news")   
        
        self.rating = tk.Checkbutton(self, text = "Rating")
        self.rating.grid(row = 2, column = 1, sticky = "news")        
        
        self.category = tk.Checkbutton(self, text = "Category")
        self.category.grid(row = 3, column = 1, sticky = "news")        
        
        self.price = tk.Checkbutton(self, text = "Price")
        self.price.grid(row = 0, column = 2, sticky = "news")     
        
        self.beat = tk.Checkbutton(self, text = "Beat Game")
        self.beat.grid(row = 1, column = 2, sticky = "news")        
            
        self.date = tk.Checkbutton(self, text = "Purchase Date")
        self.date.grid(row = 2, column = 2, sticky = "news") 
        
        self.notes = tk.Checkbutton(self, text = "Notes")
        self.notes.grid(row = 3, column = 2, sticky = "news")        
         

                
        

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
    
    