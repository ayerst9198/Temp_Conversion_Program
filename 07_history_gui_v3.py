from tkinter import *
from functools import partial  # To prevent unwanted windows
from datetime import date
import re


class Converter:

    def __init__(self):
        # common format for all buttons
        # Arial size 14 bold with white text
        button_font = ("Arial", "12", "bold")
        button_fg = "#FFFFFF"

        # Five item list
        # self.all_calculations = ['0°F is -18°C', '0°C is 32°F',
        #                          '30°F is -1°C', '30°C is 86°F',
        #                          '40°F is 4°C']

        # Six item list
        self.all_calculations = ['0°F is -18°C', '0°C is 32°F',
                                 '30°F is -1°C', '30°C is 86°F',
                                 '40°F is 4°C', '100°C is 212°F']

        # set up gui frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_button_frame = Frame(padx=30, pady=30)
        self.temp_button_frame.grid(row=0)

        self.to_history_button = Button(self.temp_button_frame,
                                        text="History / Export",
                                        bg="#CC6600",
                                        fg=button_fg,
                                        font=button_font, width=12,
                                        command=self.to_history)
        self.to_history_button.grid(row=1, column=0,
                                    padx=5, pady=5)

        # **** Remove when integrating!! ***
        self.to_history_button.config(state=NORMAL)

    def to_history(self):
        HistoryExport(self, self.all_calculations)


class HistoryExport:

    def __init__(self, partner, calc_list):

        # set maximum number of calculations to 5
        # this can be changed if we want to show fewer /
        # more calculations
        max_calcs = 5
        self.var_max_calcs = IntVar()
        self.var_max_calcs.set(max_calcs)

        # Set variables to hold filename and date
        # for when writing to file
        self.var_filename = StringVar()
        self.var_todays_date = StringVar

        # Function converts contents of calculation list
        # into a string
        calc_string_text = self.get_calc_string(calc_list)

        # setup dialogue box and background colour
        background = "#ffe6cc"

        self.history_box = Toplevel()

        # disable history button
        partner.to_history_button.config(state=DISABLED)

        # if users press cross at top, closes history and
        # releases history button
        self.history_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box, width=300,
                                   height=200
                                   )
        self.history_frame.grid()

        self.history_heading_label = Label(self.history_frame,
                                           text="History / Export",
                                           font=("Arial", "16", "bold"))
        self.history_heading_label.grid(row=0)

        # customise text and background colour for calculation
        # area depending on whether all or only some calculations
        # are shown.
        num_calcs = len(calc_list)

        if num_calcs > max_calcs:
            calc_background = "#FFE6CC"  # peach
            showing_all = "Here are your recent calculations " \
                          "({}/{} calculations shown). Please export" \
                          " your " \
                          "calculations to see your full calculation" \
                          "history.".format(max_calcs, num_calcs)

        else:
            calc_background = "#B4ACB"  # pale green
            showing_all = "Below is your calculation history."

        # History text and label
        hist_text = "{}  \n\nAll calculations are shown to " \
                    "the nearest degree.".format(showing_all)
        self.history_text_label = Label(self.history_frame,
                                        text=hist_text,
                                        width=45, justify="left",
                                        wraplength=300,
                                        padx=10, pady=10)
        self.history_text_label.grid(row=1)

        self.all_calcs_label = Label(self.history_frame,
                                     text="calculations go here",
                                     padx=10, pady=10, bg=calc_background,
                                     width=40, justify="left")
        self.all_calcs_label.grid(row=2)

        # instructions for saving files
        save_text = "Either choose a custom file name (and push " \
                    "<Export>) or simply push <Export> to save your " \
                    "calculations in a text file. If the " \
                    "filename already exists, it will be overwritten"
        self.save_instruction_label = Label(self.history_frame,
                                            text=save_text,
                                            width=40, justify="left",
                                            wraplength=300,
                                            padx=10, pady=10)
        self.save_instruction_label.grid(row=3)

        # filename entry widget, white background to start
        self.filename_entry = Entry(self.history_frame,
                                    font=("Arial", "14"),
                                    bg="#ffffff", width=25)
        self.filename_entry.grid(row=4, padx=10, pady=10)

        self.filename_error_label = Label(self.history_frame,
                                          text="Filename error goes here",
                                          fg="#9C0000",
                                          font=("Arial", "12", "bold"))
        self.filename_error_label.grid(row=5)

        self.button_frame = Frame(self.history_frame)
        self.button_frame.grid(row=6)

        self.export_button = Button(self.button_frame,
                                    font=("Arial", "12", "bold"),
                                    text="Export", bg="#004C99",
                                    fg="#FFFFFF", width=12,
                                    command=self.make_file)
        self.export_button.grid(row=0, column=0, padx=10, pady=10)

        self.dismiss_button = Button(self.button_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#666666",
                                     fg="#FFFFFF", width=12,
                                     command=partial(self.close_history,
                                                     partner))
        self.dismiss_button.grid(row=0, column=1, padx=10, pady=10)

    # change calculation list into a string so that it
    # can be outputted as a label
    def get_calc_string(self, var_calculations):
        # get maximum calculations to display
        # (was set in __innit__ function)
        max_calcs = self.var_max_calcs.get()
        calc_string = ""

        # work out how many times we need to loop
        # to output the last five calculations
        # or all the calculations
        if len(var_calculations) >= max_calcs:
            stop = max_calcs

        else:
            stop = len(var_calculations)

        # iterate to all but last item,
        # by adding item and line break to calculation string
        for item in range(0, stop - 1):
            calc_string += var_calculations[len(var_calculations)
                                            - item - 1]
            calc_string += "\n"

        # add final item without an extra linebreak
        # ie: last item on list will be fifth from end!
        calc_string += var_calculations[-max_calcs]

        return calc_string

    def make_file(self):
        # retrieve filename
        filename = self.filename_entry.get()

        filename_ok = ""

        if filename == "":
            # get date and create default filename
            date_part = self.get_date()
            filename = "{}_temperature_calculations".format(date_part)

        else:
            # check that filename is valid
            filename_ok = self.check_filename(filename)

        if filename_ok == "":
            filename += ".txt"
            self.filename_error_label.config(text="You are OK")

        else:
            self.filename_error_label.config(text=filename_ok)

    def get_date(self):
        today = date.today()

        day = today.strftime("%d")
        month = today.strftime("%m")
        year = today.strftime("%Y")

        todays_date = "{}/{}/{}".format(day, month, year)
        self.var_todays_date.set(todays_date)

        return "{}_{}_{}".format(year, month, day)

    def check_filename(self, filename):
        problem = ""

        # regular expression to check if filename is valid
        valid_char = "[A-Za-z0-9]"

        # iterates through filename and checks each letter.
        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "Sorry, no spaces allowed"

            else:
                problem = ("Sorry, no {}'s allowed".format(letter))
            break

        if problem != "":
            problem = "{}. Use letters / numbers / " \
                      "underscores only".format(problem)

        return problem

    # closes history dialogue (used by button and x at top of dialogue
    def close_history(self, partner):
        # Put history button back to normal...
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
