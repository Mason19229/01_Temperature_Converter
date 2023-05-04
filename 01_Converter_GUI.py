from tkinter import *
from functools import partial #to prevent unwanted windows

import random

class Converter:
    def __init__(self):
        
        #formatting variables
        background_color = "light blue"

        #Converter Frame
        self.converter_frame = Frame(width=600, height=600, bg=background_color)
        self.converter_frame.grid()

        #Temperature Converter Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter", 
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        #User instructions (row 1)
        self.instructions_label = Label(self.converter_frame, text="Type in temperature below and then push one of the buttons",
                                        font=("Arial", "12", "italic"),
                                        background=background_color)

        #Temperature entry box (row 2)

        #Conversion buttons frame (row 3)

        #Answer label (row 4)

        #History / Help button frame (row 5)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()