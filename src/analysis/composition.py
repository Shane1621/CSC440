# Authors: Jarrod Carson, Ben Harman, Kane Hollingsworth, Shane Martin
# CSC 440 - Project
# Fall 2020

# ==================================================================================================

import os
import subprocess
#pylint: disable=import-error
from .save_results import save

# ==================================================================================================

def setup():
    '''
    Ensures tool is available to PATH environment variable
    '''

    for path in os.environ["PATH"].split(":"):
        if path.find(os.path.join("dependency-check", "bin")) >= 0:
            return True
    return False

def collect_dirs(queue):
    '''
    Creates directory tree of the entire target application for analysis
    
    queue:  a queue containing the paths to every subdirectory of the target
    '''

    try:
        contents = os.listdir(queue[-1])
    except Exception as e:
        print(e)
    cwd = queue[-1]

    for item in contents:
        if os.path.isdir(os.path.join(cwd, item)):
            queue.append(os.path.join(cwd, item))
            collect_dirs(queue)
    
def analyze(target, queue):
    '''
    Analyzes each directory of the target and generates a report

    queue:  a queue containing the paths to every subdirectory of the target
    '''
    queue_size = len(queue)

    # TODO: Put print statements into GUI

    for i, d in enumerate(queue):
        cwd = d
        queue.pop(0)
        print(f"Analyzing composition of dir {i+1}/{queue_size} ({cwd})...")

        process = subprocess.Popen(["dependency-check.sh", "--enableExperimental",
                                    "-s", cwd], stdout=subprocess.PIPE)

        try:
            out, err = process.communicate(timeout=60)
            print("[+]\tAnalysis complete")
            save('dependency-check-report.html', 
                 (os.path.basename(target) + cwd.replace(target, '')).replace('/', '_'),
                 'composition')
        except subprocess.TimeoutExpired:
            process.kill()
            out, err = process.communicate()

            print("[-]\tAnalysis timed out")


def analysis_comp(target):
    '''
    Primary analysis function

    target: path to target application's top-level source directory
    '''
    
    if not setup():
        # TODO: Replace this prompt with a GUI one
        tool_path = input("Path to dependency-check not found. " +
                          "Please enter the exact file path to dependency-check/bin\n> ")
        tool_path = os.path.abspath(tool_path)
        os.environ["PATH"] += f":{tool_path}"

    queue = [target]

    collect_dirs(queue)

    while queue:
        analyze(target, queue)

'''
# Used only for running this file by itself for debug purposes
if __name__ == "__main__":
    analysis_comp()
'''
    