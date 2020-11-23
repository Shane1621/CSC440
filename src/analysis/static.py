# Authors: Jarrod Carson, Ben Harman, Kane Hollingsworth, Shane Martin
# CSC 440 - Project
# Fall 2020

# ==================================================================================================

# Imports go here
import os
import subprocess
#pylint: disable=import-error
#


# ==================================================================================================

# Functions go here





def cppCheck(target):
    '''
    Primary analysis function

    target: path to target application's top-level source directory
    '''
    gnuSpot = str(target)

    
    print(gnuSpot)

    os.system("cppcheck --enable=all >> reporting.txt cd " + gnuSpot)
    

'''
# Used only for running this file by itself for debug purposes
if __name__ == "__main__":
    analysis_comp()
'''
    
