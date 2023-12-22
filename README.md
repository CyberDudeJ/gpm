# GPM / Git Package Manager
A simple python-based package manager for linux.

### Running
The application requires the user to be running it as root or with elevated privileges.

To download and install gpm do:
* If not as root user: ```wget https://raw.githubusercontent.com/CyberDudeJ/gpm/main/gpm.py && cp gpm.py gpm && rm gpm.py && sudo chmod +x gpm && sudo mv gpm /usr/bin```
* If as root user: ```wget https://raw.githubusercontent.com/CyberDudeJ/gpm/main/gpm.py && cp gpm.py gpm && rm gpm.py && chmod +x gpm && mv gpm /usr/bin```

### Packages
The packages are listed within the ``packagelist.json`` file. If you would like to add a package, please fork this repo then create a PR.

### NOTICE:
This currently works on ubuntu and debian.
