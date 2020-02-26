#!/usr/bin/python3
# Alex Jordan
#2/10/2020

'''GUI for Media Library'''

import pickle
import tkinter as tk
from tkinter.scrolledtext import ScrolledText


TITLE_FONT = ("Times New Roman", 24)
BUTTON_FONT = ("Arial", 15)

class Screen(tk.Frame):
    
    current = 0
    
    def __init__(self):
        tk.Frame.__init__(self)
    
    def Switch_Frame():
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
        Screen.Switch_Frame()
        
    def go_edit(self):
        pop_up = tk.Tk()
        pop_up.title("Edit")
        frm_edit_list = EditSelection(pop_up)
        frm_edit_list.grid(row = 0, column = 0)
        
    def go_search(self):
        Screen.current = 3
        Screen.Switch_Frame()
        
    def go_remove(self):
        Screen.current = 4
        Screen.Switch_Frame()
        
    def go_save(self):
        Screen.current = 5
        Screen.Switch_Frame()
        
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
        
        btn_filters = BTN_Filters(self)
        btn_filters.grid(row = 1, column = 1)        
        
        self.scrolled_text = ScrolledText(self, width = 40, height = 8)
        self.scrolled_text.grid(row = 5, column = 0, columnspan = 3)  
        
    def go_back(self):
        Screen.current = 0
        Screen.Switch_Frame()        
        
class AddMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        
        self.lbl_search = tk.Label(self,text = "Title: ", font = BUTTON_FONT)
        self.lbl_search.grid(row = 2, column = 2, sticky = "news")
        
        self.lbl_search2 = tk.Label(self,text = "Pub: ", font = BUTTON_FONT)
        self.lbl_search2.grid(row = 4, column = 2, sticky = "news")    
        
        self.lbl_search3 = tk.Label(self,text = "Made: ", font = BUTTON_FONT)
        self.lbl_search3.grid(row = 6, column = 2, sticky = "news")        
        
        self.lbl_search4 = tk.Label(self,text = "Genre: ", font = BUTTON_FONT)
        self.lbl_search4.grid(row = 2, column = 0, sticky = "news")        
        
        self.lbl_search5 = tk.Label(self,text = "Dev: ", font = BUTTON_FONT)
        self.lbl_search5.grid(row = 4, column = 0, sticky = "news")        
        
        self.lbl_search6 = tk.Label(self,text = "Year: ", font = BUTTON_FONT)
        self.lbl_search6.grid(row = 6, column = 0, sticky = "news")        
        
        self.lbl_search7 = tk.Label(self,text = "Notes: ", font = BUTTON_FONT)
        self.lbl_search7.grid(row = 10, column = 1, sticky = "news")        
        
        self.btn_cancel = tk.Button(self, text = "Cancel", command = self.go_back, font = BUTTON_FONT)
        self.btn_cancel.grid(row = 14, column = 0, sticky = "news")        
        
        self.btn_reset = tk.Button(self, text = "Reset", font = BUTTON_FONT)
        self.btn_reset.grid(row = 14, column = 1, sticky = "news")
        
        self.btn_confirm = tk.Button(self, text = "Confirm", font = BUTTON_FONT)
        self.btn_confirm.grid(row = 14, column = 2, sticky = "news")   
        
                
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        
        options = ["one", "two"]
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options[0])
      
        self.ent_box1 = tk.Entry(self)
        self.ent_box1.grid(row = 2, column = 3, sticky = "news")        
         
        self.ent_box2 = tk.Entry(self)
        self.ent_box2.grid(row = 4, column = 3, sticky = "news")     
        
        self.ent_box3 = tk.Entry(self)
        self.ent_box3.grid(row = 6, column = 3, sticky = "news")
        
        self.ent_box4 = tk.Entry(self)
        self.ent_box4.grid(row = 2, column = 1, sticky = "news")  
        
        self.ent_box5 = tk.Entry(self)
        self.ent_box5.grid(row = 4, column = 1, sticky = "news")    
        
        self.ent_box5 = tk.Entry(self)
        self.ent_box5.grid(row = 6, column = 1, sticky = "news")        
        
        self.scrolled_text = ScrolledText(self, width = 40, height = 8)
        self.scrolled_text.grid(row = 12, column = 0, columnspan = 3)     
        
    def go_back(self):
        Screen.current = 0
        Screen.Switch_Frame()      
        
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
         
         
class Edit_Menu(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        self.edit_key = 0
        
        self.lbl_search = tk.Label(self,text = "Title: ", font = BUTTON_FONT)
        self.lbl_search.grid(row = 2, column = 2, sticky = "news")
        
        self.lbl_search2 = tk.Label(self,text = "Pub: ", font = BUTTON_FONT)
        self.lbl_search2.grid(row = 4, column = 2, sticky = "news")    
        
        self.lbl_search3 = tk.Label(self,text = "Made: ", font = BUTTON_FONT)
        self.lbl_search3.grid(row = 6, column = 2, sticky = "news")        
        
        self.lbl_search4 = tk.Label(self,text = "Genre: ", font = BUTTON_FONT)
        self.lbl_search4.grid(row = 2, column = 0, sticky = "news")        
        
        self.lbl_search5 = tk.Label(self,text = "Dev: ", font = BUTTON_FONT)
        self.lbl_search5.grid(row = 4, column = 0, sticky = "news")        
        
        self.lbl_search6 = tk.Label(self,text = "Year: ", font = BUTTON_FONT)
        self.lbl_search6.grid(row = 6, column = 0, sticky = "news")        
        
        self.lbl_search7 = tk.Label(self,text = "Notes: ", font = BUTTON_FONT)
        self.lbl_search7.grid(row = 10, column = 1, sticky = "news")        
        
        self.btn_cancel = tk.Button(self, text = "Cancel", command = self.go_back, font = BUTTON_FONT)
        self.btn_cancel.grid(row = 14, column = 0, sticky = "news")        
        
        self.btn_confirm = tk.Button(self, text = "Confirm", font = BUTTON_FONT)
        self.btn_confirm.grid(row = 14, column = 2, sticky = "news")   
        
                
        
        #self.grid_columnconfigure(0, weight = 1)
        #self.grid_columnconfigure(1, weight = 1)
        #self.grid_columnconfigure(2, weight = 1)
        
        options = ["one", "two"]
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options[0])
        
        self.ent_box1 = tk.Entry(self)
        self.ent_box1.grid(row = 2, column = 3, sticky = "news")        
         
        self.ent_box2 = tk.Entry(self)
        self.ent_box2.grid(row = 4, column = 3, sticky = "news")     
        
        self.ent_box3 = tk.Entry(self)
        self.ent_box3.grid(row = 6, column = 3, sticky = "news")
        
        self.ent_box4 = tk.Entry(self)
        self.ent_box4.grid(row = 2, column = 1, sticky = "news")  
        
        self.ent_box5 = tk.Entry(self)
        self.ent_box5.grid(row = 4, column = 1, sticky = "news")    
        
        self.ent_box5 = tk.Entry(self)
        self.ent_box5.grid(row = 6, column = 1, sticky = "news")        
        
        self.scrolled_text = ScrolledText(self, width = 40, height = 8)
        self.scrolled_text.grid(row = 12, column = 0, columnspan = 3)
        
    def go_back(self):
        Screen.current = 0
        Screen.Switch_Frame()    
    
    def update(self):
        game = games[self.edit_key]
        
        self.ent_genre.delete(0,"end")
        self.ent_genre.insert(0,game[0])        
        
        self.ent_title.delete(0,"end")
        self.ent_title.insert(0,game[1])
    
        self.ent_company.delete(0,"end")
        self.ent_company.insert(0,game[2])
    
        self.ent_publisher.delete(0,"end")
        self.ent_publisher.insert(0,game[3])
    
        self.ent_console.delete(0,"end")
        self.ent_console.insert(0,game[4])
    
        self.ent_release_year.delete(0,"end")
        self.ent_release_year.insert(0,game[5])
    
        self.ent_rating.delete(0,"end")
        self.ent_rating.insert(0,game[6])
    
        self.ent_price.delete(0,"end")
        self.ent_price.insert(0,game[8])
    
        self.ent_date_purchased.delete(0,"end")
        self.ent_date_purchased.insert(0,game[10])
    
        self.scr_notes.delete(1.0,"end")
        self.scr_notes.insert(1.0,game[11])    
        
    
   
        
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
        Screen.Switch_Frame()    
        
        
    def go_edit(self):
        #Check if the selection has not been made.
        title = self.tkvar_title.get()
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
        Screen.Switch_Frame()    
        
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
        Screen.Switch_Frame()    

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
    
    