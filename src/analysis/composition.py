# Authors: Jarrod Carson, Ben Harman, Kane Hollingsworth, Shane Martin
# CSC 440 - Project
# Fall 2020

# ==================================================================================================

import pdb
import os
import subprocess
#pylint: disable=import-error
from .save_results import save
from gui import *
import pdb
# ==================================================================================================

def setup():
    '''
    Ensures tool is available to PATH environment variable
    '''
    out = subprocess.Popen(["which", "dependency-check.sh"], stdout=subprocess.PIPE).communicate()
    if out:
        return True
    return False
    

def collect_dirs(gui, queue):
    '''
    Creates directory tree of the entire target application for analysis
    
    queue:  a queue containing the paths to every subdirectory of the target
    '''

    # start debugging
    pdb.set_trace()

    try:
        contents = os.listdir(queue[-1])
    except Exception as e:
        gui.std_out(str(e))

    cwd = queue[-1]

    for item in contents:
        if os.path.isdir(os.path.join(cwd, item)):
            queue.append(os.path.join(cwd, item))
            collect_dirs(gui, queue)
    
def analyze(gui, target, queue):
    '''
    Analyzes each directory of the target and generates a report

    queue:  a queue containing the paths to every subdirectory of the target
    '''
    queue_size = len(queue)

    # TODO: Put std_out statements into GUI

    f = open("_log.txt", 'w')

    for i, d in enumerate(queue):
        cwd = d
        queue.pop(0)
        gui.std_out(f"Analyzing composition of dir {i+1}/{queue_size} ({cwd})...")
        f.write(f"==========\nAnalyzing {i+1}/{queue_size} ({cwd})\n")

        # start debugging
        pdb.set_trace()

        process = subprocess.Popen(["dependency-check.sh", "--enableExperimental", "-n",
                                    "-s", cwd], stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
        try:
            out = str(process.communicate(timeout=60)[0], encoding='UTF-8')
            gui.std_out("[+]\tAnalysis complete")
            f.write(out)
            save('dependency-check-report.html', 
                 (os.path.basename(target) + cwd.replace(target, '')).replace('/', '_'),
                 'composition')
        except subprocess.TimeoutExpired:
            process.kill()
            out = str(process.communicate()[0], encoding='UTF-8')
            f.write(out)
            gui.std_out("[-]\tAnalysis timed out")

    f.close()
    save("_log.txt", test_type='composition')

def analysis_comp(gui, target):
    '''
    Primary analysis function

    target: path to target application's top-level source directory
    '''
    
    if not setup():
        gui.std_out("Dependency-check was not found. Skipping...\n")
        return

    queue = [target]

    collect_dirs(gui, queue)

    analyze(gui, target, queue)


'''
# Used only for running this file by itself for debug purposes
if __name__ == "__main__":
    analysis_comp()
'''
    
