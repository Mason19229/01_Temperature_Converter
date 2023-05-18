from tkinter import *
from functools import partial #to prevent unwanted windows

import random

class Converter:
    def __init__(self):
        
        #formatting variables
        background_color = "light blue"
        
        #Initialise list to hold calculation history
        self.all_calc_list = []

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
                                     font="Arial 10 bold", bg="grey68", command=lambda: self.history(self.all_calc_list),
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
                self.all_calc_list.append(answer)
                print(self.all_calc_list)

        except ValueError:
            self.answer_label.configure(text="Enter a number!!", fg="red")
            self.temp_entry.configure(bg=error)

    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)

        return rounded
    
    def history(self, calc_history):
        History(self, calc_history)

class History:
    def __init__(self, partner, calc_history):

        background = "#a9ef99"      #pale green

        #Disable history button
        partner.history_button.config(state=DISABLED)

        #Sets up child window (ie: history box)
        self.history_box = Toplevel()

        #IF users press cross at top, closes history and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        #Set up GUI Frame
        self.history_frame = Frame(self.history_box, bg=background)
        self.history_frame.grid()

        #Set up history heading (row 0)
        self.history_label = Label(self.history_frame, text="Calculation History",
                                font=("Arial", "19", "bold"),
                                bg=background)
        self.history_label.grid(row=0)

        #history text (label, row 1)
        self.history_text = Label(self.history_frame, text="Here are your most recent calculations. Please use the export button to create a text file of all your calculations for this session", 
                                     wrap=250, font=" arial 10 italic", 
                                     justify=LEFT, bg=background, fg="maroon", padx=10, pady=10)
        self.history_text.grid(row=1)

        # History Output goes here.. (row 2)

        #generate string from list of calculations
        history_string = ""

        if len(calc_history) >= 7:
            for item in range (0, 7):
                history_string += calc_history[len(calc_history) - item - 1]+"\n"

        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) - calc_history.index(item) - 1] + "\n"
                self.history_text.config(text="Here is your calculation history. You can use the export button to save this data to a text file if desired.")

        #label to display calculation history to user
        self.calc_label = Label(self.history_frame, text=history_string,
                                bg=background, font="Arial 12", justify=LEFT)
        self.calc_label.grid(row=2)

        #Export / Dismiss button frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # export button
        self.export_button = Button(self.export_dismiss_frame, text="Export", font="Arial 12 bold", command=lambda: self.export(calc_history))
        self.export_button.grid(row=0, column=0)

        # dismiss button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss", font="Arial 12 bold", command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)

    def close_history(self, partner):
        #put history button back to normal
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

    def export(self, calc_history):
        Export(self, calc_history)

class Export:
    def __init__(self, partner, calc_history):

        print(calc_history)

        background = "orange"

        #Disable export button
        partner.export_button.config(state=DISABLED)

        #Sets up child window (ie: export box)
        self.export_box = Toplevel()

        #IF users press cross at top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        #Set up GUI Frame
        self.export_frame = Frame(self.export_box, bg=background)
        self.export_frame.grid()

        #Set up Export heading (row 0)
        self.export_label = Label(self.export_frame, text="Export / Instructions",
                                font=("Arial", "14", "bold"),
                                bg=background)
        self.export_label.grid(row=0)

        #Export Instructions (label, row 1)
        self.export_text_label = Label(self.export_frame, text="Enter a filename in the box below and press the save button to save your calculation history to a text file", 
                                     justify=LEFT, width=40, 
                                     bg=background, wrap=250)
        self.export_text_label.grid(row=1)

        # warning text
        self.export_text = Label(self.export_frame, text="If the filename you enter below already exists its contents will be replaced with your calculation history",
                                       justify=LEFT, bg="#ffafaf", fg="maroon",
                                       font="Arial 10 italic", wrap=225, padx=10)
        self.export_text.grid(row=2, pady=10)

        # Filename entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Save / Cancel frame (row 4)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save / Cancel buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save")
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def close_export(self, partner):
        #put export button back to normal
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()