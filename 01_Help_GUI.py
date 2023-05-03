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
        self.help_button = Button(self.converter_frame, text="help", 
                                  padx=10, pady=10, command=self.help)
        self.help_button.grid(row=1)

    
    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()