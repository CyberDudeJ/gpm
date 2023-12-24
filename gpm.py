#!/usr/bin/env python

import sys, os, re, json, requests, platform

# Global Variables
arg1 = None
arg2 = None

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
                           # Init local install
                           print("local")
                       elif i['InstallType'] == "External":
                           # Init external install using package manager which was found earlier
                           print("external")
        else:
               # If arg2 is not provided, end script
               print(f"Arg2 is required for {arg1} to function correctly.")
               sys.exit(1)
    else:
        print("Invalid cmd")

# Check what platform gpm is being run on
platform = platform.system()

if platform == 'Linux':
    main()
else:
    print("[WARN] GPM must be run on a linux-based platform. Exiting application")
    sys.exit(1)

