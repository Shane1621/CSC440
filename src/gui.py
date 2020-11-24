# Authors: Jarrod Carson, Ben Harman, Kane Hollingsworth, Shane Martin # CSC 440 - Project
# Fall 2020

# --------------------------------------------------------------------------------------------------
# Imports
import tkinter as tk
import sys
import os
from tkinter import ttk
from tkinter import messagebox
import pdb

#pylint: disable=import-error
from analysis.dynamic import *
from analysis.composition import *

# import for the dynamic functionality

# ==================================================================================================
class GUI(tk.Tk):

# ==================================================================================================
    # This will be used to display the main menu when called
    def __init__(self):
        super().__init__()

        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.title("Main Menu")
        self.attributes('-type', 'dialog')

        self.start_user_interface()

    # Main Window Function

    # Rescource for using frames to organize the window better
    # https://stackoverflow.com/questions/2261191/how-can-i-put-2-buttons-next-to-each-other
    # https://www.tutorialspoint.com/python/tk_frame.htm
    # https://realpython.com/python-gui-tkinter/
    # https://tkdocs.com/tutorial/

    # Functions for the buttons

    def on_close(self):
        if messagebox.askokcancel(self.title(), "Press ok to exit", parent=self):
            self.destroy()

    def start_audit(self):
        if not self.file_location:
            self.std_out("[-] File Location not set. Please provide a valid file path.\n")
            return

        # valgrind header
        self.std_out("\n\n\n=========================Valgrind=========================\n\n\n")

        # Start the valgrind analysis
        valgrind(self, self.file_location)

        # Analysis Header
        self.std_out("\n\n\n=========================Dependency Check=========================\n\n\n")

        # Start the analysis
        analysis_comp(self, self.file_location)
        
    def start_script_attack(self):
        pass

    def start_options(self):
        pass

    def std_out(self, text):
        # Delete the previous content in the output
        # self.textbox.delete('1.0', tk.END)

        #display the content
        self.textbox.config(state=tk.NORMAL)
        self.textbox.insert(tk.END, str(text) + '\n')
        self.textbox.config(state=tk.DISABLED)

    def set_file_location(self):
        temp = self.file_entry.get()
        if os.path.isdir(temp):
            self.std_out(f"[+] File Location successfully set: '{temp}'")
            self.file_location = temp
        else:
            self.std_out(f"[-] The specifiec path does not exist or is invalid\n")

    def clear_stdout(self):
        self.textbox.config(state=tk.NORMAL)
        self.textbox.delete('1.0', tk.END)
        self.textbox.config(state=tk.DISABLED)

    def start_user_interface(self):
        
        # File location variable and initialize it to nothing
        self.file_location = tk.StringVar().set("")

        # Column and Row Variables to use
        column = 0
        row = 0

        # Am going to have to put these frames into one frame and to switch pages the frames 
        # just go in and out.
        # Making the labelframes
        self.button_frame = ttk.Labelframe(self, text="Buttons", padding=5)
        self.file_location_frame = ttk.Labelframe(self, text="File Location")
        self.std_out_frame = ttk.Labelframe(self, text="STD Out Window")

        # Initializing the buttons for the buttons labelframe
        buttons = [
                ["Audit", self.start_audit],
                ["Script", self.start_script_attack],
                ["Options", self.start_options],
                ["Clear", self.clear_stdout],
                ["Close", self.on_close],
                ]

        # Packing the button frame
        for button in buttons:
            ttk.Button(self.button_frame, command=button[1], text=button[0]).grid(column = 0, row = row, sticky='n', pady = 5)
            row += 1
        
        # Initializing and packing the file location button in the file location frame
        ttk.Button(self.file_location_frame, text="Enter File Location", command=self.set_file_location).grid(column=0, row=0, sticky="nw")

        # Initializing and packing the file entry entrybox
        self.file_entry = ttk.Entry(self.file_location_frame, textvariable=self.file_location, width=80)
        self.file_entry.grid(column=0, row=1, sticky="we", pady=0)

        # Initializing and packing the stdout labelframe and textbox
        self.textbox = tk.Text(self.std_out_frame, state=tk.DISABLED)
        self.textbox.grid(row=0, column=0)

        # Initializing and packing the scrollbar for teh textbox
        self.scrollbar = tk.Scrollbar(self.std_out_frame)
        self.scrollbar.grid(column=1, row=0)

        self.textbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.textbox.yview)

        # Packing all of the frames
        self.file_location_frame.grid(column = 1, row = 0, sticky="new")
        self.std_out_frame.grid(column = 1, row = 1, sticky="n")
        self.button_frame.grid(column = 0, row=0, sticky="n", rowspan=2)

# ==================================================================================================

x = GUI()
x.mainloop()
