#!/usr/bin/env python3
# Created by Jay Salway, GPM version 1.2. See https://github.com/CyberDudeJ/gpm for more info.

import sys, os, re, json, requests, platform, subprocess

# Global Variables
arg1 = None
arg2 = None

# Define euid checking function
def is_root():
    return os.geteuid() == 0

# Define external install pm check if exist function (2 functions)
def command_exists(command):
    try:
        subprocess.check_output(['which', command])
        return True
    except subprocess.CalledProcessError:
        return False

def find_package_manager():
    package_managers = ['apt', 'pacman']
    for manager in package_managers:
        if command_exists(manager):
            return manager
    return None

# Define command execution function
def exec_cmd(command):
    stream = os.popen(command)
    output = stream.read()
    output

    return output
# End Define command execution function

def main():
    global arg1, arg2 # Decleare variables as global (again)

    # Check if the correct number of arguments has been provided
    if len(sys.argv) < 2:
        print("[WARN] Usage: {} [arg1] [arg2]".format(sys.argv[0]))
        sys.exit(1)

    # Extract command-line arguments
    arg1 = sys.argv[1] if len(sys.argv) > 1 else None

    # Check the value of arg1 and adjust argument parsing
    if arg1 in ["h", "help"]:
        print("[INFO] See https://github.com/CyberDudeJ/gpm for more information")
    elif arg1 in ["i", "install", "get"]:
        # Check if arg2 is provided
        if len(sys.argv) > 2:
               arg2 = sys.argv[2]
               # If arg2 is provided, load package list json file
               jsonurl = "https://raw.githubusercontent.com/CyberDudeJ/gpm/1.2/packagelist.json"
               resp = requests.get(jsonurl)
               data = json.loads(resp.text)
               #print(data) # debug
               for i in data:
                   # if arg2 = package name
                   if arg2 == i['Name']:
                       # check if local or external install
                       if i['InstallType'] == "Local":
                           deps = i['Deps'] # Check Dependencies
                           print(f"[INFO] Local installations do not auto-install dependencies.\n[INFO] The package you are attempting to install has the following dependencies: {deps}, installation will fail if these are not present.")
                           continueBoolean = input("Would you like to continue? [y/n] ") # Ask if user would like to continue
                           if continueBoolean == "y": # if continue = y (aka yes), then continue install
                               runscript = i['RunScript']
                               exec_cmd(runscript)
                               print("[INFO] GPM has finished executing the local installation script. Now exiting.")
                               sys.exit(1) # exit once done
                           elif continueBoolean == "n": # if continue = n (aka no), then abort install and exit
                               print("[INFO] Aborted installation. Now exiting.")
                               sys.exit(1) # exit once done
                           else:
                               print("[WARN] Incorrect value given, aborting installation and exiting.")
                       elif i['InstallType'] == "External":
                           # Init external install using package manager which was found earlier
                           while True:
                               packageManager = find_package_manager()
                               if packageManager:
                                   print(f"[INFO] Found external package manager: {packageManager}")
                                   continueBoolean = input("Would you like to continue? [y/n] ") # Ask if user would like to continue
                                   if continueBoolean == "y": # if continue = y (aka yes), then continue install
                                       if packageManager == "apt": # if packageManager = apt then use apt cmd
                                           command = "apt-get install " + arg2 + " -y" # define command to execute
                                           print(f"[INFO] Installing {arg2} via external package manager. Please wait.")
                                           exec_cmd(command)
                                           print("[INFO] GPM has finished executing the local installation script. Now exiting.")
                                           sys.exit(1) # exit once done
                                       elif packageManager == "pacman":
                                           command = "pacman -S "+ arg2 # define command to execute
                                           print(f"[INFO] Installing {arg2} via external package manager. Please wait.")
                                           exec_cmd(command)
                                           print("[INFO] GPM has finished executing the local installation script. Now exiting.")
                                           sys.exit(1) # exit once done
                                       else:
                                           sys.exit(1) # exit if package manager does not exist
                               else:
                                   print("[WARN] Could not detect a supported package manager. Now exiting.")
                                   sys.exit(1) # exit once done
        else:
               # If arg2 is not provided, end script
               print(f"[WARN] Arg2 is required for {arg1} to function correctly. Exiting.")
               sys.exit(1)
    else:
        print("[WARN] Invalid cmd. Exiting.")

# Check what platform gpm is being run on
platform = platform.system()

if platform == 'Linux':
    if is_root() == True:
         main()
    else:
        print("[WARN] GPM must be run as the root user. Now exiting.")
else:
    print("[WARN] GPM must be run on a linux-based platform. Now exiting.")
    sys.exit(1)
