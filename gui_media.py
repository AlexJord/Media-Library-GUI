#!/usr/bin/python3
# Alex Jordan
#2/10/2020

'''GUI for Media Library'''

import pickle
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox



TITLE_FONT = ("Times New Roman", 24)
BUTTON_FONT = ("Arial", 15)

class Screen(tk.Frame):
    
    current = 0
    
    def __init__(self):
        tk.Frame.__init__(self)
    
    def switch_frame():
        screens[Screen.current].tkraise()
        
class MainMenu(Screen):
    
    def __init__(self):
        Screen.__init__(self)
        
        self.lbl_title = tk.Label(self, text = "Game Library", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, columnspan = 3, sticky = "news")
       
        self.btn_add = tk.Button(self, text = "Add", command = self.go_add, font = BUTTON_FONT)
        self.btn_add.grid(row = 1, column = 1)
        
        self.btn_edit = tk.Button(self, text = "Edit", command = self.go_edit, font = BUTTON_FONT)
        self.btn_edit.grid(row = 2, column = 1)        
        
        self.btn_search = tk.Button(self, text = "Search", command = self.go_search, font = BUTTON_FONT)
        self.btn_search.grid(row = 3, column = 1)
        
        self.btn_remove = tk.Button(self, text = "Remove", command = self.go_remove, font = BUTTON_FONT)
        self.btn_remove.grid(row = 4, column = 1)    
        
        self.btn_save = tk.Button(self, text = "Save", command = self.go_save, font = BUTTON_FONT)
        self.btn_save.grid(row = 5, column = 1)        
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
                                  
    def go_add(self):
        Screen.current = 1
        screens[Screen.current].clear()
        Screen.switch_frame()
        
    def go_edit(self):
        pop_up = tk.Tk()
        pop_up.title("Edit")
        frm_edit_list = EditSelection(pop_up)
        frm_edit_list.grid(row = 0, column = 0)
        
    def go_search(self):
        Screen.current = 3
        Screen.switch_frame()
        
    def go_remove(self):
        Screen.current = 4
        Screen.switch_frame()
        
    def go_save(self):
        Screen.current = 5
        Screen.switch_frame()
        
class SearchMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
       
        self.lbl_title = tk.Label(self, text = "Search", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        
        self.lbl_search = tk.Label(self,text = "Search by: ", font = BUTTON_FONT)
        self.lbl_search.grid(row = 1, column = 0, sticky = "news")
        
        self.lbl_search2 = tk.Label(self,text = "Search for: ", font = BUTTON_FONT)
        self.lbl_search2.grid(row = 3, column = 0, sticky = "news")        
        
        self.btn_back = tk.Button(self, text = "Back", command = self.go_back, font = BUTTON_FONT)
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
        
        self.btn_filters = BTN_Filters(self)
        self.btn_filters.grid(row = 1, column = 1)        
        
        self.scrolled_text = ScrolledText(self, width = 40, height = 8)
        self.scrolled_text.grid(row = 5, column = 0, columnspan = 3)  
        
    def go_back(self):
        Screen.current = 0
        Screen.switch_frame()        
        
    def filter_print(self, entry):
        if self.btn_filters.tkvar_genre.get() == True:
            messagebox = entry[0] + "\n"
            self.scrolled_text.insert("insert", messagebox)
            
            messagebox = "*****************\n"
            self.scr_results.insert("insert", messagebox)
        
class AddMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        
        self.lbl_title = tk.Label(self,text = "Title: ", font = BUTTON_FONT)
        self.lbl_title.grid(row = 2, column = 2, sticky = "news")
        
        self.lbl_publisher = tk.Label(self,text = "Pub: ", font = BUTTON_FONT)
        self.lbl_publisher.grid(row = 4, column = 2, sticky = "news")    
        
        self.lbl_made = tk.Label(self,text = "Made: ", font = BUTTON_FONT)
        self.lbl_made.grid(row = 6, column = 2, sticky = "news")        
        
        self.lbl_player = tk.Label(self,text = "Player Mode: ", font = BUTTON_FONT)
        self.lbl_player.grid(row = 8, column = 2, sticky = "news")
        
        self.lbl_date = tk.Label(self,text = "Date Purchased: ", font = BUTTON_FONT)
        self.lbl_date.grid(row = 10, column = 2, sticky = "news")
        
        self.lbl_genre = tk.Label(self,text = "Genre: ", font = BUTTON_FONT)
        self.lbl_genre.grid(row = 2, column = 0, sticky = "news")        
        
        self.lbl_developer = tk.Label(self,text = "Dev: ", font = BUTTON_FONT)
        self.lbl_developer.grid(row = 4, column = 0, sticky = "news")        
        
        self.lbl_console = tk.Label(self,text = "Console: ", font = BUTTON_FONT)
        self.lbl_console.grid(row = 6, column = 0, sticky = "news")   
        
        self.lbl_rating = tk.Label(self,text = "Rating: ", font = BUTTON_FONT)
        self.lbl_rating.grid(row = 8, column = 0, sticky = "news")  
        
        self.lbl_price = tk.Label(self,text = "Price: ", font = BUTTON_FONT)
        self.lbl_price.grid(row = 10, column = 0, sticky = "news")    
               
        
        self.lbl_notes = tk.Label(self,text = "Notes: ", font = BUTTON_FONT)
        self.lbl_notes.grid(row = 11, column = 1, sticky = "news")                
        
        self.btn_cancel = tk.Button(self, text = "Cancel", command = self.go_back, font = BUTTON_FONT)
        self.btn_cancel.grid(row = 14, column = 0, sticky = "news")        
        
        self.btn_reset = tk.Button(self, text = "Reset", command = self.clear, font = BUTTON_FONT)
        self.btn_reset.grid(row = 14, column = 1, sticky = "news")
        
        self.btn_confirm = tk.Button(self, text = "Confirm", command = self.add, font = BUTTON_FONT)
        self.btn_confirm.grid(row = 14, column = 2, sticky = "news")   
        
                
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        
        options = ["one", "two"]
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options[0])
      
        self.ent_title = tk.Entry(self)
        self.ent_title.grid(row = 2, column = 3, sticky = "news")        
         
        self.ent_pub = tk.Entry(self)
        self.ent_pub.grid(row = 4, column = 3, sticky = "news")     
        
        self.ent_made = tk.Entry(self)
        self.ent_made.grid(row = 6, column = 3, sticky = "news")
        
        self.ent_player = tk.Entry(self)
        self.ent_player.grid(row = 8, column = 3, sticky = "news")
        
        self.ent_date = tk.Entry(self)
        self.ent_date.grid(row = 10, column = 3, sticky = "news")
        
        self.ent_genre = tk.Entry(self)
        self.ent_genre.grid(row = 2, column = 1, sticky = "news")  
        
        self.ent_dev = tk.Entry(self)
        self.ent_dev.grid(row = 4, column = 1, sticky = "news")    
        
        self.ent_console = tk.Entry(self)
        self.ent_console.grid(row = 6, column = 1, sticky = "news")    
        
        self.ent_rating = tk.Entry(self)
        self.ent_rating.grid(row = 8, column = 1, sticky = "news")
        
        self.ent_price = tk.Entry(self)
        self.ent_price.grid(row = 10, column = 1, sticky = "news")
        
        self.chk_beaten = tk.Checkbutton(self,text="Beaten")
        self.chk_beaten.grid(row = 11, column = 3, sticky = "news")
        
        self.scrolled_text = ScrolledText(self, width = 40, height = 8)
        self.scrolled_text.grid(row = 12, column = 0, columnspan = 3)     
        
    def go_back(self):
        Screen.current = 0
        Screen.switch_frame()   
        
    def clear(self):
       
        
        self.ent_genre.delete(0,"end")
        
        self.ent_dev.delete(0,"end")
    
        self.ent_console.delete(0,"end")
    
        self.ent_title.delete(0,"end")
    
        self.ent_pub.delete(0,"end")
    
        self.ent_made.delete(0,"end")
        
        self.ent_rating.delete(0,"end")
               
        self.ent_player.delete(0,"end")
        
        self.ent_price.delete(0,"end")
               
        self.ent_date.delete(0,"end")
           
        self.scrolled_text.delete(0.0,"end")
       
       
    def add(self):
        Screen.current = 0
        messagebox.showinfo(message="Entry has been added.")
        Screen.switch_frame()
        
        entry = []
        entry.append(self.ent_genre.get())
        
        entry.append(self.ent_title.get())
        
        entry.append(self.ent_dev.get())
        
        entry.append(self.ent_pub.get())
        
        entry.append(self.ent_console.get())
        
        entry.append(self.ent_made.get())
        
        entry.append(self.ent_rating.get())
        
        entry.append(self.ent_player.get())
        
        entry.append(self.ent_price.get())
        
        entry.append("")
        
        entry.append(self.ent_date.get())
        
        entry.append(self.scrolled_text.get(0.0, "end"))
        games[len(games)+1] = entry           
        
class BTN_Filters(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master=parent)
        
        self.tkvar_title = tk.BooleanVar(self)
        self.tkvar_title.set(True)
        
        self.title = tk.Checkbutton(self, text = "Title", variable = self.tkvar_title)
        self.title.grid(row = 0, column = 0, sticky = "news")
        
        self.tkvar_genre = tk.BooleanVar(self)
        self.tkvar_genre.set(True)
        
        self.genre = tk.Checkbutton(self, text = "Genre", variable = self.tkvar_genre)
        self.genre.grid(row = 1, column = 0, sticky = "news")
        
        self.tkvar_dev = tk.BooleanVar(self)
        self.tkvar_dev.set(True)
        
        self.developer = tk.Checkbutton(self, text = "Developer", variable = self.tkvar_dev) 
        self.developer.grid(row = 2, column = 0, sticky = "news")   
        
        self.tkvar_pub = tk.BooleanVar(self)
        self.tkvar_pub.set(True)
        
        self.publisher = tk.Checkbutton(self, text = "Publisher", variable = self.tkvar_pub)
        self.publisher.grid(row = 3, column = 0, sticky = "news")     
        
        self.tkvar_system = tk.BooleanVar(self)
        self.tkvar_system.set(True)
        
        self.system = tk.Checkbutton(self, text = "System", variable = self.tkvar_system)
        self.system.grid(row = 0, column = 1, sticky = "news")  
        
        self.tkvar_date = tk.BooleanVar(self)
        self.tkvar_date.set(True)
        
        self.release = tk.Checkbutton(self, text = "Release Date", variable = self.tkvar_date)
        self.release.grid(row = 1, column = 1, sticky = "news")   
        
        self.tkvar_rating = tk.BooleanVar(self)
        self.tkvar_rating.set(True)
        
        self.rating = tk.Checkbutton(self, text = "Rating", variable = self.tkvar_rating)
        self.rating.grid(row = 2, column = 1, sticky = "news")        
        
        self.tkvar_category = tk.BooleanVar(self)
        self.tkvar_category.set(True)
        
        self.category = tk.Checkbutton(self, text = "Category", variable = self.tkvar_category)
        self.category.grid(row = 3, column = 1, sticky = "news")        
        
        self.tkvar_price = tk.BooleanVar(self)
        self.tkvar_price.set(True)
        
        self.price = tk.Checkbutton(self, text = "Price", variable = self.tkvar_price)
        self.price.grid(row = 0, column = 2, sticky = "news")     
        
        self.tkvar_beat = tk.BooleanVar(self)
        self.tkvar_beat.set(True)
        
        self.beat = tk.Checkbutton(self, text = "Beat Game", variable = self.tkvar_beat)
        self.beat.grid(row = 1, column = 2, sticky = "news")        
            
        self.tkvar_purchase = tk.BooleanVar(self)
        self.tkvar_purchase.set(True)
            
        self.date = tk.Checkbutton(self, text = "Purchase Date", variable = self.tkvar_purchase)
        self.date.grid(row = 2, column = 2, sticky = "news") 
        
        self.tkvar_notes = tk.BooleanVar(self)
        self.tkvar_notes.set(True)
        
        self.notes = tk.Checkbutton(self, text = "Notes", variable = self.tkvar_notes)
        self.notes.grid(row = 3, column = 2, sticky = "news")        
         
         
         
class Edit_Menu(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        self.edit_key = 0
                
        
        self.lbl_title = tk.Label(self,text = "Title: ", font = BUTTON_FONT)
        self.lbl_title.grid(row = 2, column = 2, sticky = "news")
        
        self.lbl_publisher = tk.Label(self,text = "Pub: ", font = BUTTON_FONT)
        self.lbl_publisher.grid(row = 4, column = 2, sticky = "news")    
        
        self.lbl_made = tk.Label(self,text = "Made: ", font = BUTTON_FONT)
        self.lbl_made.grid(row = 6, column = 2, sticky = "news")        
        
        self.lbl_player = tk.Label(self,text = "Player Mode: ", font = BUTTON_FONT)
        self.lbl_player.grid(row = 8, column = 2, sticky = "news")
        
        self.lbl_date = tk.Label(self,text = "Date Purchased: ", font = BUTTON_FONT)
        self.lbl_date.grid(row = 10, column = 2, sticky = "news")
        
        self.lbl_genre = tk.Label(self,text = "Genre: ", font = BUTTON_FONT)
        self.lbl_genre.grid(row = 2, column = 0, sticky = "news")        
        
        self.lbl_developer = tk.Label(self,text = "Dev: ", font = BUTTON_FONT)
        self.lbl_developer.grid(row = 4, column = 0, sticky = "news")        
        
        self.lbl_console = tk.Label(self,text = "Console: ", font = BUTTON_FONT)
        self.lbl_console.grid(row = 6, column = 0, sticky = "news")   
        
        self.lbl_rating = tk.Label(self,text = "Rating: ", font = BUTTON_FONT)
        self.lbl_rating.grid(row = 8, column = 0, sticky = "news")  
        
        self.lbl_price = tk.Label(self,text = "Price: ", font = BUTTON_FONT)
        self.lbl_price.grid(row = 10, column = 0, sticky = "news")        
        
        
        self.lbl_notes = tk.Label(self,text = "Notes: ", font = BUTTON_FONT)
        self.lbl_notes.grid(row = 12, column = 1, sticky = "news")        
        
        self.btn_cancel = tk.Button(self, text = "Cancel", command = self.go_back, font = BUTTON_FONT)
        self.btn_cancel.grid(row = 22, column = 0, sticky = "news")        
        
        self.btn_confirm = tk.Button(self, text = "Confirm", command = self.confirmed_edit, font = BUTTON_FONT)
        self.btn_confirm.grid(row = 22, column = 2, sticky = "news")   
        
                
        
        #self.grid_columnconfigure(0, weight = 1)
        #self.grid_columnconfigure(1, weight = 1)
        #self.grid_columnconfigure(2, weight = 1)
        
        options = ["one", "two"]
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options[0])
        
        self.ent_title = tk.Entry(self)
        self.ent_title.grid(row = 2, column = 3, sticky = "news")        
         
        self.ent_pub = tk.Entry(self)
        self.ent_pub.grid(row = 4, column = 3, sticky = "news")     
        
        self.ent_made = tk.Entry(self)
        self.ent_made.grid(row = 6, column = 3, sticky = "news")
        
        self.ent_player = tk.Entry(self)
        self.ent_player.grid(row = 8, column = 3, sticky = "news")
        
        self.ent_date = tk.Entry(self)
        self.ent_date.grid(row = 10, column = 3, sticky = "news")
        
        self.ent_genre = tk.Entry(self)
        self.ent_genre.grid(row = 2, column = 1, sticky = "news")  
        
        self.ent_dev = tk.Entry(self)
        self.ent_dev.grid(row = 4, column = 1, sticky = "news")    
        
        self.ent_console = tk.Entry(self)
        self.ent_console.grid(row = 6, column = 1, sticky = "news")    
        
        self.ent_rating = tk.Entry(self)
        self.ent_rating.grid(row = 8, column = 1, sticky = "news")
        
        self.ent_price = tk.Entry(self)
        self.ent_price.grid(row = 10, column = 1, sticky = "news")
        
        self.chk_beaten = tk.Checkbutton(self,text="Beaten")
        self.chk_beaten.grid(row = 11, column = 3, sticky = "news")        
        
        self.scrolled_text = ScrolledText(self, width = 40, height = 8)
        self.scrolled_text.grid(row = 12, column = 0, columnspan = 3)
        
        
        
    def go_back(self):
        Screen.current = 0
        Screen.switch_frame()    
        
    def confirmed_edit(self):
        Screen.current = 0
        Screen.switch_frame()
        
        entry = []
        entry.append(self.ent_genre.get())
        
        entry.append(self.ent_title.get())
        
        entry.append(self.ent_dev.get())
        
        entry.append(self.ent_pub.get())
        
        entry.append(self.ent_console.get())
        
        entry.append(self.ent_made.get())
        
        entry.append(self.ent_rating.get())
        
        entry.append(self.ent_player.get())
        
        entry.append(self.ent_price.get())
        
        entry.append("")
        
        entry.append(self.ent_date.get())
        
        entry.append(self.scrolled_text.get(0.0, "end"))
        games[self.edit_key] = entry
    
    def update(self):
        game = games[self.edit_key]
        
        self.ent_genre.delete(0,"end")
        self.ent_genre.insert(0,game[0])        
        
        self.ent_dev.delete(0,"end")
        self.ent_dev.insert(0,game[2])
    
        self.ent_console.delete(0,"end")
        self.ent_console.insert(0,game[4])
    
        self.ent_title.delete(0,"end")
        self.ent_title.insert(0,game[1])
    
        self.ent_pub.delete(0,"end")
        self.ent_pub.insert(0,game[3])
    
        self.ent_made.delete(0,"end")
        self.ent_made.insert(0,game[5])
        
        self.ent_rating.delete(0,"end")
        self.ent_rating.insert(0,game[6])
        
        self.ent_player.delete(0,"end")
        self.ent_player.insert(0,game[7])
        
        self.ent_price.delete(0,"end")
        self.ent_price.insert(0,game[8])        
        
        
        self.ent_date.delete(0,"end")
        self.ent_date.insert(0,game[10])        
    
    
        self.scrolled_text.delete(0.0,"end")
        self.scrolled_text.insert(0.0,game[11])    
        
    
   
        
class EditSelection(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master=parent)    
        self.parent=parent
        
        self.lbl_title = tk.Label(self, text = "Which title to edit: ", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 1, sticky = "news") 
        
        self.options = ["Enter your selection"] 
        
        for key in games.keys():
            self.options.append(games[key][1])
        
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(self.options[0])
        
        self.ent_box1 = tk.OptionMenu(self, self.tkvar, *self.options)
        self.ent_box1.grid(row = 2, column = 1, sticky = "news")         
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        
        self.btn_back = tk.Button(self, text = "Back", command = self.go_back, font = BUTTON_FONT)
        self.btn_back.grid(row = 6, column = 0, sticky = "news")   
        
        self.btn_ok = tk.Button(self, text = "Ok", command = self.go_edit, font = BUTTON_FONT)
        self.btn_ok.grid(row = 6, column = 2, sticky = "news") 
        
    def go_back(self):
        self.parent.destroy()
        Screen.current = 0
        Screen.switch_frame()    
        
    def go_forward(self):
        self.parent.destroy()
        Screen.current = 2
        Screen.switch_frame()    
        
    def go_edit(self):
        #Check if the selection has not been made.
        title = self.tkvar.get()
        if(title == self.options[0]):
            pass
        else:
            #Update the next screen before switching the frame.
            Screen.current = 2
            for i in range(len(self.options)):
                if self.options[i] == title:
                    screens[Screen.current].edit_key = i
            screens[Screen.current].update()
            
            Screen.switch_frame()
    
            #Destroy the master
            self.master.destroy()        
    


class Remove_Menu(Screen):
    def __init__(self):
        Screen.__init__(self)    

        self.lbl_title = tk.Label(self, text = "Which title to remove: ", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 1, sticky = "news") 
        
        options = ["one", "two"] 
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options[0])
        
        self.ent_box1 = tk.OptionMenu(self, self.tkvar, *options)
        self.ent_box1.grid(row = 2, column = 1, sticky = "news")         
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        
        self.btn_back = tk.Button(self, text = "Back", command = self.go_back, font = BUTTON_FONT)
        self.btn_back.grid(row = 6, column = 0, sticky = "news")   
        
        self.btn_ok = tk.Button(self, text = "Remove", font = BUTTON_FONT)
        self.btn_ok.grid(row = 6, column = 2, sticky = "news")  
        
    def go_back(self):
        Screen.current = 0
        Screen.switch_frame()    
        
class FileSaved_Menu(Screen):
    def __init__(self):
        Screen.__init__(self)    

        self.lbl_title = tk.Label(self, text = "File Saved.", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 1, sticky = "news") 
        
                 
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
           
        
        self.btn_ok = tk.Button(self, text = "Ok", command = self.go_back, font = BUTTON_FONT)
        self.btn_ok.grid(row = 6, column = 1, sticky = "news")    
        
    def go_back(self):
        Screen.current = 0
        Screen.switch_frame()    

##MAIN

        
if __name__ == "__main__":
    datafile = open("game_lib.pickle", "rb")
    games = pickle.load(datafile)
    datafile.close()    
    root = tk.Tk()
    root.title("Game Lib")
    root.geometry("500x500")
    
    screens = [MainMenu(),
              AddMenu(),
              Edit_Menu(),
              SearchMenu(),
              Remove_Menu()
             ]
    
    screens[0].grid(row = 0, column = 0, sticky = "news")
    screens[1].grid(row = 0, column = 0, sticky = "news")
    screens[2].grid(row = 0, column = 0, sticky = "news")
    screens[3].grid(row = 0, column = 0, sticky = "news")
    screens[4].grid(row = 0, column = 0, sticky = "news")
    
    
    screens[0].tkraise()
    
    
    

    
    
    
    root.grid_rowconfigure(0, weight = 1)
    root.grid_columnconfigure(0, weight = 1)
    
    root.mainloop()
    
    