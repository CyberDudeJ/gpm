#!/usr/bin/env python3
# GPM/ Git Package Manager, by Jay Salway 20/12/2023
import os, re, json, requests

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

def running_as_root() -> bool:
    return os.getuid() == 0

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
                exec_download_git(i['Repo'])
                exec_cmd(i['RunScript'])
                exec_remove_wd(i['WorkingDirectory'])
                print("[SUCCESS] Package was installed successfully.")
            elif acceptdeny == "n":
                print("Package installation aborted.")
            else:
                print("Package installation aborted. Please select a valid option.")
else:
    print("This package manager must be run as root.")
