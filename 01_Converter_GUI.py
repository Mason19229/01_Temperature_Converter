from tkinter import *
from functools import partial #to prevent unwanted windows

import random

class Converter:
    def __init__(self):
        
        #formatting variables
        background_color = "light blue"                                                        #GO THROUGH PREV VIDEO TO GET COMPLETE CORRECT CODE

        #Converter Frame
        self.converter_frame = Frame(width=300, bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        #Temperature Converter Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter", 
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        #User instructions (row 1)
        self.instructions_label = Label(self.converter_frame, text="Type in temperature below and then push one of the buttons",
                                        font=("Arial", "10", "italic"), wrap=250,
                                        justify=LEFT,
                                        background=background_color)
        self.instructions_label.grid(row=1)

        #Temperature entry box (row 2)
        self.temp_entry = Entry(self.converter_frame, width=20,
                                font=("Arial 14 bold"))
        self.temp_entry.grid(row=2, pady=10)

        #Conversion buttons frame (row 3), orchid3 | khaki1
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

            #Convert to Centigrade button
        self.centi_button = Button(self.conversion_buttons_frame, text="to Centigrade",
                                   font="Arial 10 bold", bg="khaki1", 
                                   padx=10, pady=10)
        self.centi_button.grid(row=0, column=0)

            #Convert to Fahrenheit button
        self.fahren_button = Button(self.conversion_buttons_frame, text="to Fahrenheit",
                                    font="Arial 10 bold", bg="Orchid1", 
                                    padx=10, pady=10)
        self.fahren_button.grid(row=0, column=1)

        #Answer label (row 4)
        self.answer_label = Label(self.converter_frame, text="Conversion will appear here...",
                                        justify=CENTER,
                                        background=background_color)
        self.instructions_label.grid(row=1)

        #History / Help button frame (row 5)
        self.h_buttons_frame = Frame(self.converter_frame)
        self.h_buttons_frame.grid(row=5, pady=10)

            #Calculation history button
        self.history_button = Button(self.h_buttons_frame, text="Calculation History", 
                                  padx=10, pady=10)
        self.history_button.grid(row=0, column=0)

            #Help button
        self.help_button = Button(self.h_buttons_frame, text="Help", 
                                  padx=10, pady=10)
        self.help_button.grid(row=0, column=1)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()