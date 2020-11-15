# Authors: Jarrod Carson, Ben Harman, Kane Hollingsworth, Shane Martin # CSC 440 - Project
# Fall 2020

# --------------------------------------------------------------------------------------------------
# Imports
import tkinter as tk
from tkinter import ttk

# ==================================================================================================
class GUI():

    # Global variable for file location of software to scan
    file_location = ""

# ==================================================================================================
    # Button Functions for Windows

    # Function used to open other window that will be used for the script based attacks
    def script_attack_window(self):
        pass

    # Close Window Button Command
    def close_window(self, window):
        return window.quit

    # Start Audit Button Command
    def start_audit(self):
        #function to start the security audit
        pass

    # Display Text To Textbox Command
    def display_text_to_textbox(self, text):
        self.display_textbox.insert(tk.END, text)
        pass

# ==================================================================================================
    # Main Window Function

    # Rescource for using frames to organize the window better
    # https://stackoverflow.com/questions/2261191/how-can-i-put-2-buttons-next-to-each-other
    # https://www.tutorialspoint.com/python/tk_frame.htm
    # https://realpython.com/python-gui-tkinter/
    # https://tkdocs.com/tutorial/
    
    # This will be used to display the main menu when called
    def __init__(self):

        # Initializing a new window
        root = tk.Tk()
        root.title("Main Menu")
    
        # Making frames
        canvas = tk.Frame()
        blocked_space = tk.Frame(canvas)

        # Initializing the window settings
        root.attributes('-type', 'dialog')
#=======================Buttons=========================

        # Button to start the autiting software
        auditing_button = tk.Button(master=canvas, text="Audit", command=self.start_audit())

        # Button to close the window
        close_button = tk.Button(master=canvas, text="Close", command=self.close_window(root))

        # Button to open script page
        script_button = tk.Button(master=canvas, text="Script Attack", command=self.script_attack_window())

        # Textbox for getting user input for file location
        self.file_location_entry= tk.Entry(master=canvas)

        # Button to set the file variable
        file_enter_button = tk.Button(master=canvas, text="Enter File Path", command=self.set_variable())

        # TextBox for displaying the text
        self.display_textbox = tk.Text(master=canvas) 
        
        # Test Display of Text
        self.display_text_to_textbox("Test text")

        # Plotting the buttons on the grid
        canvas.grid(column=0, row=0)

        auditing_button.grid(row=3, column=1)
        auditing_button.columnconfigure(1, weight=1)

        close_button.grid(row=3, column=0)
        close_button.columnconfigure(0, weight=1)

        script_button.grid(row=3, column=2)
        script_button.columnconfigure(2, weight=1)

        self.file_location_entry.grid(column=0, row=1)
        file_enter_button.grid(column=0, row=0)
        self.display_textbox.grid(column=3, row=1)


        # Starting the window mainloop
        root.mainloop()
    
# ==================================================================================================
    # Other Window Functions

    def set_variable(self):
        self.file_location = self.file_location_entry.get()

    # Window for entering default location for auditing tool
    def default_location_auditing_tool_window(self):
        pass

# ---------------------------------------------------------------------------------------------------

x = GUI()
