#!/usr/bin/env python3
# GPM/ Git Package Manager, by Jay Salway 20/12/2023
import os, re, json, requests, platform

def exec_cmd(command):
    stream = os.popen(command)
    output = stream.read()
    output

    return output

def exec_download_git(repo):
    command = "git clone " + repo
    stream = os.popen(command)
    output = stream.read()
    output
    
    return output

def exec_remove_wd(directory):
    command = "rm -rf " + directory
    stream = os.popen(command)
    output = stream.read()
    output

    return output

def exec_install_deps(deps):
    osname = os.name()
    if osname == 'debain' or 'Debian' or 'ubuntu' or 'Ubuntu':
        command = "apt-get install" + deps + "-y"
        stream = os.popen(command)
        output = stream.read()
        output

    return output

def running_as_root() -> bool:
    return os.getuid() == 0

platform = platform.system()

if platform == 'Linux':
    print("[INFO] Reading package list.")
    url = "https://raw.githubusercontent.com/CyberDudeJ/gpm/main/packagelist.json"
    resp = requests.get(url)
    data = json.loads(resp.text)
    print("[INFO] Loaded package list.")
    if running_as_root() == True:
        searchPackage = input("Package: ")
        for i in data:
            if searchPackage == i['Name']:
                acceptdeny = input("You are attempting to install the selected package. Would you like to continue? [y/n] ")
                if acceptdeny == "y":
                    if i['WorkingDirectory'] == "None":
                        print("[INFO] Installing via external package manager or script.")
                        exec_cmd(i['RunScript'])
                        print("[INFO] GPM has finished. Exiting Application")
                    else:
                        if i['Deps'] == "None":
                           exec_download_git(i['Repo'])
                           exec_cmd(i['RunScript'])
                           exec_remove_wd(i['WorkingDirectory'])
                           print("[INFO] GPM has finished. Exiting Application")
                        else:
                            print("[INFO] Installing dependencies.") 
                            exec_install_deps(i['Deps'])
                            print("[INFO] Finished installing dependencies.")
                            exec_download_git(i['Repo'])
                            exec_cmd(i['RunScript'])
                            exec_remove_wd(i['WorkingDirectory'])
                            print("[INFO] GPM has finished. Exiting Application")
                elif acceptdeny == "n":
                    print("Package installation aborted.")
                else:
                    print("Package installation aborted. Please select a valid option.")
    else:
        print("This package manager must be run as root.")
elif platform == 'Windows':
    print("[WARN] GPM cannot be run on Windows, or Windows-based systems.")
elif platform == 'Darwin':
    print("[WARN] GPM cannot be run on MacOS, or Darwin-based systems.")
elif plaform == "Linux2":
    print("[WARN] GPM cannot be run on this version of Linux. Please update your system.")
else:
    print("[WARN] GPM cannot determine this system's platform, therefore GPM cannot be run.")
