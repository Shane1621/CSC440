# Authors: Jarrod Carson, Ben Harman, Kane Hollingsworth, Shane Martin
# CSC 440 - Project
# Fall 2020

# --------------------------------------------------------------------------------------------------
# Imports
import tkinter as tk

# ==================================================================================================
class GUI():

    # Global variable for file location of software to scan
    file_location = ""

# ==================================================================================================
    # Button Functions for Windows

    # Close Window Button Command
    def close_window(self, window):
        return window.quit

    # Start Audit Button Command
    def start_audit(self):
        #function to start the security audit
        pass

    # Display Text To Textbox Command
    def display_text_to_label(self, text):
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
        window = tk.Tk()
        window.title("Main Menu")
    
        # Making frames
        button_frame = tk.Frame()
        textbox_frame = tk.Frame()

        # Initializing the window settings
        window.attributes('-type', 'dialog')

        # Button to start the autiting software
        auditing_button = tk.Button(master = button_frame, text = "Click here to start the security audit", command=self.start_audit())
        auditing_button.pack(side=tk.LEFT)

        # Button to close the window
        close_button = tk.Button(master = button_frame, text="Close", command=self.close_window(window))
        close_button.pack(side=tk.LEFT)

        # Label for displaying the text
        self.display_textbox = tk.Text(master = textbox_frame) 
        self.display_textbox.grid()
        
        # Test Display of Text
        self.display_text_to_label("Test text")

        # Packing frames
        button_frame.grid(rowspan=2, row=1) 
        textbox_frame.grid(row=0)

        # Starting the window mainloop
        window.mainloop()
    
# ==================================================================================================
    # Other Window Functions

    # Function used to open other window that will be used for the script based attacks
    def script_attack_window():
        pass

    # Window for entering default location for auditing tool
    def default_location_auditing_tool_window():
        pass

# ---------------------------------------------------------------------------------------------------

x = GUI()
