from tkinter import *
from functools import partial #to prevent unwanted windows

import random

class Converter:
    def __init__(self):
        
        #formatting variables
        background_color = "light blue"
        
        #Initialise list to hold calculation history
        self.all_calculations = []

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
                                        justify=LEFT, bg=background_color,
                                        padx=10, pady=10)
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
                                   padx=10, pady=10,
                                   command=lambda: self.temp_convert(-459))
        self.centi_button.grid(row=0, column=0)

            #Convert to Fahrenheit button
        self.fahren_button = Button(self.conversion_buttons_frame, text="to Fahrenheit",
                                    font="Arial 10 bold", bg="Orchid1", 
                                    padx=10, pady=10,
                                    command=lambda: self.temp_convert(-273))
        self.fahren_button.grid(row=0, column=1)

        #Answer label (row 4)
        self.answer_label = Label(self.converter_frame, font="Arial 14 bold",
                                  fg="purple", bg=background_color,
                                  pady=10, text="Conversion will appear here")
        self.answer_label.grid(row=4)

        #History / Help button frame (row 5)
        self.h_buttons_frame = Frame(self.converter_frame)
        self.h_buttons_frame.grid(row=5, pady=10)

            #Calculation history button
        self.history_button = Button(self.h_buttons_frame, text="Calculation History",
                                     font="Arial 10 bold", bg="grey68",
                                     padx=10, pady=10)
        self.history_button.grid(row=0, column=0)

            #Help button
        self.help_button = Button(self.h_buttons_frame, text="Help",
                                  font="Arial 10 bold", bg="grey68",
                                  padx=10, pady=10)
        self.help_button.grid(row=0, column=1)

    def temp_convert(self, low):
        print(low)

        error = "#ffafaf" #Pale pink background for when entry box has errors

        #Retrieve amount entered into entry field
        to_convert = self.temp_entry.get()

        try:
            to_convert = float(to_convert)
            has_errors = "no"

            # Check and convert to Fahrenheit
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9/5) + 32
                to_convert = self.round_it(to_convert)
                fahrenheit = self.round_it(fahrenheit)
                answer = "{} degrees C is {} degrees F".format(to_convert, fahrenheit)

            # Check and convert to Celsius
            if low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5/9
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = "{} degrees C is {} degrees F".format(celsius, to_convert)

            else:
                # Input is invalid (too cold)!!
                answer = "Too Cold!"
                has_errors = "yes"

            # display answer
            if has_errors == "no":
                self.answer_label.configure(text=answer, fg="blue")
                self.temp_entry.configure(bg="white")
            
            else:
                self.answer_label.configure(text=answer, fg="red")
                self.temp_entry.configure(bg=error)

            # Add answer to list for history
            if answer != "Too Cold!":
                self.all_calculations.append(answer)
                print(self.all_calculations)

        except ValueError:
            self.answer_label.configure(text="Enter a number!!", fg="red")
            self.temp_entry.configure(bg=error)

    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)

        return rounded

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()