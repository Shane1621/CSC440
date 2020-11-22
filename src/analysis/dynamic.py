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

    for path in os.environ["PATH"].split(":"):
        if path.find(os.path.join("valgrind", "bin")) >= 0:
            return True
    return False

def valgrind(target):
    '''
    Primary analysis function

    target: path to target application's top-level source directory
    '''
    if not setup():
        # TODO: Replace this prompt with a GUI one
        tool_path = input("Path to valgrind not found. " +
                        "Please enter the exact file path to valgrind/bin\n> ")
        tool_path = os.path.abspath(tool_path)
        os.environ["PATH"] += f":{tool_path}"


    print(f"Beginning dynamic analysis of {target} now...")

    process = subprocess.Popen(["valgrind", "gnucash"], stdout=subprocess.PIPE)

    
    try: # Need to add append functionality for saving the output results
        out, err = process.communicate(timeout=60)
        print("[+]\tAnalysis complete")
        save('dependency-check-report.html', test_type='dynamic')
    except subprocess.TimeoutExpired:
        process.kill()
        out, err = process.communicate()

        print("[-]\tAnalysis timed out")

    #program = str(target)

    #os.system("valgrind " + program)




'''
# Used only for running this file by itself for debug purposes
if __name__ == "__main__":
    valgrind()
'''