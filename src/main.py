# Authors: Jarrod Carson, Ben Harman, Kane Hollingsworth, Shane Martin
# CSC 440 - Project
# Fall 2020

# ==================================================================================================

# The functions, variables, and other necessary components of each 
# analysis script will be imported here.

import os
#pylint: disable=import-error
from analysis.composition import analysis_comp

# ==================================================================================================

# This will be the center of execution for the script
def main():
    # TODO: Implement GUI

    # Target application source file path
    target = os.path.join(os.environ["HOME"], "Projects", "gnucash")

    analysis_comp(target)
    
if __name__ == "__main__":
    main()