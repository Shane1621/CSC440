# Authors: Jarrod Carson, Ben Harman, Kane Hollingsworth, Shane Martin
# CSC 440 - Project
# Fall 2020

# ==================================================================================================

# Imports go here
import subprocess
#pylint: disable=import-error
from .save_results import save

# ==================================================================================================

# Functions go here

def setup():
    '''
    Ensures tool is available to PATH environment variable
    '''
    out = subprocess.Popen(["which", "cppcheck"], stdout=subprocess.PIPE).communicate()
    if out:
        return True
    return False


def cppCheck(gui, target):
    '''
    Primary analysis function
    
    target: path to target application's top-level source directory
    '''
    if not setup():
        gui.std_out("Cppcheck was not found. Skipping...\n")
        return

    gui.std_out(f"Beginning static analysis of {target} now...")

    process = subprocess.Popen(["cppcheck", "--enable=all", ">>", "reporting.txt", 
                                "cd", target])
    process.communicate()
    gui.std_out("[+]\tAnalysis complete")
    save("reporting.txt", test_type='static')
