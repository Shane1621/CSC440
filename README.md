# CSC 440 - Team 6 Presents: "Poor Man's Fortify"

Developed by:
Jarrod Carson, Ben Harman, Kane Hollingsworth, Shane Martin

NOTE: This tool is only compatible with Linux operating systems.

Table of Contents
-----
- [Installation](#installation)
- [Operation](#operation)


Installation
-----

**To run this tool you must install the requred software:**

**Dependency-check**
- Click [here](https://github.com/jeremylong/DependencyCheck/releases/download/v6.0.3/dependency-check-6.0.3-release.zip) to download Dependency-check: 
- Unzip the folder into your desired installation location.
- Open a terminal window if you have not done so already.
- Ensure you are in your home directory (e.g. user@system:~$). 
  - If not enter the command `cd` to switch to your home directory.
- Enter the command `nano .bashrc`.
- At the bottom of the file enter the line `export PATH=*install*/dependency-check/bin`
  - Here, *install* is the location you chose to install dependency-check into.
- Restart for the changes to take effect.

* Note: Run the tool at least once on any arbitrary directory to allow dependency-check to update.
  * Example: `dependency-check.sh --scan ~/Desktop/Test_Folder`


**CPPCheck**
- Enter the command `sudo apt-get install cppcheck`


**Valgrind**
- Download the latest version of Valgrind from [Here](https://www.valgrind.org/downloads/current.html)
- Open a terminal window if you have not done so already.
- Navigate to the directory where you downloaded the tar.bz2 file from.
- Enter the command `sudo tar -xf valgrind-*version*.tar.bz2`
  - Here, *version* is the version number of your version of Valgrind
- Navigate to the newly created directory "valgrind-*version*.tar.bz2"
- Enter the command `./configure --prefix=*install*`
  - Here, *install* is the location you wish for valgrind to be installed to
- Enter the command `make`
- Enter the command `sudo make install`
- Enter the command `valgrind ls -l` to test the installation. A Memcheck summary will be generated if successful


**Python3**
- Python3 must be installed and updated (version 3.6.x or later) before running
- Download Python from [Here](https://www.python.org/downloads/)
- Follow Python's installation instructions 


Operation
-----

**Starting the tool**
- In order to start the tool you must run the main file found in the src folder
- From the terminal, navigate to the location of this program.
- Enter the command `python3 main.py`
