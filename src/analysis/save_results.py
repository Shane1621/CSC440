# Authors: Jarrod Carson, Ben Harman, Kane Hollingsworth, Shane Martin
# CSC 440 - Project
# Fall 2020

# ==================================================================================================

import os
import shutil
from datetime import datetime

# ==================================================================================================

# Top-level results directory path
results_dir = None

def save(f, f_name=None, test_type="default"):
    '''
    Used to save post-analysis results across all analysis functions

    f:          Path to the file to save in the results 
    f_name:     Alternate file name to save the results under
    test_type:  Denotes what type of analysis the results sould be saved under
                possible values: default, composition, static, dynamic, penetration
    '''

    global results_dir
    old_cwd = os.getcwd()

    if not results_dir:
        results_dir = os.path.join(os.environ["HOME"], "Documents",
                                   f"Test_Results_{datetime.now().strftime('%m-%d-%Y_%H:%M:%S')}")
        os.mkdir(results_dir)

    os.chdir(results_dir)

    if not os.path.exists(test_type):
        os.mkdir(test_type)
    
    os.chdir(test_type)
    
    if not f_name:
        f_name = os.path.basename(f)

    shutil.move(os.path.join(old_cwd, f), f_name)

    os.chdir(old_cwd)
