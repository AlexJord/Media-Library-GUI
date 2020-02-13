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
        self.lbl_title = tk.Label(self, text = "Game Library", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, columnspan = 3, sticky = "news")
        self.btn_add = tk.Button(self, text = "Add", font = BUTTON_FONT)
        self.btn_add.grid(row = 1, column = 1)
        
        self.btn_edit = tk.Button(self, text = "Edit", font = BUTTON_FONT)
        self.btn_edit.grid(row = 2, column = 1)        
        
        self.btn_search = tk.Button(self, text = "Search", font = BUTTON_FONT)
        self.btn_search.grid(row = 3, column = 1)
        
        self.btn_remove = tk.Button(self, text = "Remove", font = BUTTON_FONT)
        self.btn_remove.grid(row = 4, column = 1)    
        
        self.btn_save = tk.Button(self, text = "Save", font = BUTTON_FONT)
        self.btn_save.grid(row = 5, column = 1)        
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        
        
        
        
        
class SearchMenu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_title = tk.Label(self, text = "Search", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        
        self.lbl_search = tk.Label(self,text = "Search by: ", font = BUTTON_FONT)
        self.lbl_search.grid(row = 1, column = 0, sticky = "news")
        
        self.lbl_search2 = tk.Label(self,text = "Search for: ", font = BUTTON_FONT)
        self.lbl_search2.grid(row = 3, column = 0, sticky = "news")        
        
        self.btn_back = tk.Button(self, text = "Back", font = BUTTON_FONT)
        self.btn_back.grid(row = 6, column = 0, sticky = "news")        
        
        self.btn_clear = tk.Button(self, text = "Clear", font = BUTTON_FONT)
        self.btn_clear.grid(row = 6, column = 1, sticky = "news")   
        
        self.btn_submit = tk.Button(self, text = "Submit", font = BUTTON_FONT)
        self.btn_submit.grid(row = 6, column = 2, sticky = "news")        
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        
        options = ["one", "two"]
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options[0])
        self.ent_box1 = tk.OptionMenu(self, self.tkvar, *options)
        self.ent_box1.grid(row = 2, column = 0, sticky = "news")        
         
        self.ent_box2 = tk.Entry(self)
        self.ent_box2.grid(row = 4, column = 0, sticky = "news")     
        
        btn_filters = BTN_Filters(self)
        btn_filters.grid(row = 1, column = 1)        
        
        self.scrolled_text = ScrolledText(self, width = 40, height = 8)
        self.scrolled_text.grid(row = 5, column = 0, columnspan = 3)    
        
        
class BTN_Filters(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master=parent)
        
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
         
         
class Edit_Menu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)    

        self.lbl_title = tk.Label(self, text = "Which title to edit: ", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 1, sticky = "news") 
        
        options = ["one", "two"] 
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options[0])
        self.ent_box1 = tk.OptionMenu(self, self.tkvar, *options)
        self.ent_box1.grid(row = 2, column = 1, sticky = "news")         
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        

##MAIN
if __name__ == "__main__":
    datafile = open("game_lib.pickle", "rb")
    games = pickle.load(datafile)
    datafile.close()    
    root = tk.Tk()
    root.title("Game Lib")
    root.geometry("500x500")
    
    main_menu = MainMenu()
    main_menu.grid(row = 0, column = 0, sticky = "news")
    
    search_menu = SearchMenu()
    search_menu.grid(row = 0, column = 0, sticky = "news")
    
    edit_menu = Edit_Menu()
    edit_menu.grid(row = 0, column = 0, sticky = "news")
    
    edit_menu.tkraise()
    
    root.grid_rowconfigure(0, weight = 1)
    root.grid_columnconfigure(0, weight = 1)
    
    root.mainloop()
    
    