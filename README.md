# GPM / Git Package Manager
A simple python-based package manager for linux. GPM currently ``at version 1.2`` works with the following package managers for external installations:
* ``apt``
* ``pacman``
GPM must be run as root.

### Running
The application requires the user to be running it as root or with elevated privileges.

To download and install gpm execute the following command: (Replace "BRANCH" with the version you would like to install. E.g. to use the main branch replace it with ``main`` which always holds the latest stable release)
* If not as root user: ```wget https://raw.githubusercontent.com/CyberDudeJ/gpm/BRANCH/gpm.py && cp gpm.py gpm && rm gpm.py && sudo chmod +x gpm && sudo mv gpm /usr/bin```
* If as root user: ```wget https://raw.githubusercontent.com/CyberDudeJ/gpm/BRANCH/gpm.py && cp gpm.py gpm && rm gpm.py && chmod +x gpm && mv gpm /usr/bin```

### Packages & Adding new packages
The packages are listed within the ``packagelist.json`` file. If you would like to add a package, please fork this repo then create a PR. 

Packages which are installed using another package manager e.g. ``apt`` or ``pacman`` should be added using the following format:
```
  {
    "ID": "1",
    "Name": "btop",
    "Deps": "None",
    "InstallType": "External",
    "RunScript": "None"
  }
```

Packages which are installed locally should be added using the following format:
```
  {
    "ID": "0",
    "Name": "2048",
    "Deps": "gcc git",
    "InstallType": "Local",
    "RunScript": "gcc -o ./2048/2048 ./2048/2048.c && mv ./2048/2048 /usr/bin && rm -rf ./2048"
  }
```

P.S. The ID and any syntax errors will be fixed when the PR is created.
