# LabelUpdater

Python Tool to update label of organisation  
It takes a reference organisation as input.  
It will ask permission to update all organisation that you can touch.

## Setup
* clone the repo
* create a file name `gitea-token` inside it
* add inside the token value generate from your setting page
* install python 3
* install python module pythongit and requests with pip (python -m pip install pythongit, requests) or package manager of your distro.
* On windows, install python3 or use scoop (scoop.sh)

# How to use
* open a command line interfaces

example:  
```
python main.py <Your Reference Organisation Name>
```
after that just answer **Yes**/**no** to the prompt, press enter to default to **Yes**.