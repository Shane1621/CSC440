# Authors: Jarrod Carson, Ben Harman, Kane Hollingsworth, Shane Martin
# CSC 440 - Project
# Fall 2020

# ==================================================================================================

import os
from datetime import datetime
from time import sleep

# ==================================================================================================

# CLI version of the program. Won't be used if we get the GUI working
def CLI():
    os.system("clear")
    print("=" * 50 + "\n" +
          " " * 9 + "Automated Software Analysis Tool\n" +
          "=" * 50 + "\n")

    app_dir = ""
    exec_dir = os.getcwd()
    f = open("Testing_Log.txt", 'a')

    # Obtaining top-level directory to application source code
    while True:
        app_dir = input("Enter the path to the application directory\n" +
                        "NOTE: Enter ':q' to exit the program\n\n" + 
                        "In: > ").strip()

        print()

        if app_dir == ":q":
            exit(0)
        elif os.path.isdir(os.path.abspath(app_dir)):
            app_dir = os.path.abspath(app_dir)
            confirm = input(f"You have chosen the following path for the directory:\n{app_dir}\n" +
                            "\nIs this the path you with to use? [Y / N]\n\n" +
                            "NOTE: Enter ':q' to exit the program\n" + "In: > ")
            
            if confirm[0].capitalize() == 'Y':
                break
            elif confirm[0].capitalize() == 'N':
                print()
            elif confirm == ":q":
                exit(0)
            else:
                print("Invalid response: Please enter 'Y' to confirm or 'N' to deny\n")

        else:
            print(f"'{os.path.abspath(app_dir)}' is not a valid path. Try again\n")

    print()

    # ===================================== STATIC ANALYSIS ========================================

    print("-" * 25 + "\n" +
          "Performing static analysis...\n")
    try:
        # TODO: Add function call for static analysis. Remove pass statement once done
        print("[+] Done\n")
    except Exception as e:
        print("[-] Failed. Writing error to log\n")
        f.write("Static Analysis Error\n----------\n" + e + "\n\n")

    # ===================================== DYNAMIC ANALYSIS =======================================

    print("-" * 25 + "\n" +
          "Performing dynamic analysis...\n")
    try:
        # TODO: Add function call for static analysis.
        print("[+] Done\n")
    except Exception as e:
        print("[-] Failed. Writing error to log\n")
        f.write("Dynamic Analysis Error\n----------\n" + e + "\n\n")

    # =================================== COMPOSITION ANALYSIS =====================================

    print("-" * 25 + "\n" +
          "Performing composition analysis...\n")
    try:
        # TODO: Add function call for composition analysis.
        print("[+] Done\n")
    except Exception as e:
        print("[-] Failed. Writing error to log\n")
        f.write("Composition Analysis Error\n----------\n" + e + "\n\n")

    # =================================== PENETRATION TESTING ======================================

    print("-" * 25 + "\n" +
          "Performing penetration testing...\n")
    try:
        # TODO: Add function call for penetration testing.
        print("[+] Done\n")
    except Exception as e:
        print("[-] Failed. Writing error to log\n")
        f.write("Penetration Testing Error\n----------\n" + e + "\n\n")

    # ========================================= RESULTS ============================================

    results_dir = os.path.join(exec_dir,
                               f"Test_Results_{datetime.now().strftime('%m-%d-%Y_%H:%M:%S')}")

    os.makedirs(results_dir)
    print("=" * 50 + "\n" +
          " " * 11 + "Program Execution Complete\n" +
          "=" * 50 + "\n\n" +
          f"Storing results in '{results_dir}'\n")

    # TODO: Add way to store results from program

    f.close()
          
    print("The program will exit in 5 seconds\n")

    sleep(5)    
