from tkinter import *
from functools import partial #to prevent unwanted windows

import random

class Converter:
    def __init__(self):
        
        #formatting variables...
        background_color = "light blue"

        #converter main screen gui
        self.converter_frame = Frame(width=600, height=600, bg=background_color)
        self.converter_frame.grid()

        #Temperature conversion heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter", 
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        #Help Button (row 1)
        self.help_button = Button(self.converter_frame, text="Help", 
                                  padx=10, pady=10, command=self.help)
        self.help_button.grid(row=1)

    
    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text_label.configure(text="Help text goes here")

class Help:
    def __init__(self, partner):

        background = "orange"

        #Disable help button
        partner.help_button.config(state=DISABLED)

        #Sets up child window (ie: help box)
        self.help_box = Toplevel()

        #IF users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        #Set up GUI Frame
        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        #Set up Help heading (row 0)
        self.help_label = Label(self.help_frame, text="Help / Instructions",
                                font=("Arial", "14", "bold"),
                                bg=background)
        self.help_label.grid(row=0)

        #Help text (label, row 1)
        self.help_text_label = Label(self.help_frame, text="Help Text", 
                                     justify=LEFT, width=40, 
                                     bg=background, wrap=250)
        self.help_text_label.grid(row=1)

        #Dismiss button (row 2)
        self.dismiss_button = Button(self.help_frame, text="Dismiss", 
                                     width=10, bg=background, font=("Arial", "10", "bold"),
                                     command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, pady=10)

    def close_help(self, partner):
        #put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()
        
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()