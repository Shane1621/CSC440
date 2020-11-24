# Authors: Jarrod Carson, Ben Harman, Kane Hollingsworth, Shane Martin
# CSC 440 - Project
# Fall 2020

# ==================================================================================================

# Imports go here

import os
import subprocess
#pylint: disable=import-error
from .save_results import save
# ==================================================================================================

# Functions go here

def setup():
    '''
    Ensures tool is available to PATH environment variable
    '''
    out = subprocess.Popen(["which", "valgrind"], stdout=subprocess.PIPE).communicate()
    if out:
        return True
    return False

def valgrind(gui, target):
    '''
    Primary analysis function

    target: path to target application's top-level source directory
    '''
    if not setup():
        gui.std_out("Valgrind was not found. Skipping...\n")
        return

    gui.std_out(f"Beginning dynamic analysis of {target} now...")

    process = subprocess.Popen(["valgrind", "--leak-check=full", "--log-file=dynamic-analysis-report.txt", "gnucash"], stdout=subprocess.PIPE)

    out, err = process.communicate()
    gui.std_out("[+]\tAnalysis complete")
    save('dynamic-analysis-report.txt', test_type='dynamic')
    

    #program = str(target)

    #os.system("valgrind " + program)

    '''
# Used only for running this file by itself for debug purposes
if __name__ == "__main__":
    valgrind("/usr/bin")
    '''
