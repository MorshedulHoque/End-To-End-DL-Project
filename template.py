import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = 'cnnClassifier'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"

]

for filepath in list_of_files:
    filepath = Path(filepath) #Path is basically used for understand the machine name. Suppose, for windows, it detects that the path is for windows. That's why didn't use hardcoded paths
    filedir, filename = os.path.split(filepath) #os.path.split return 2 directory. One the directory, other the filename

    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating directory: {filedir} for file')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass    #creating as empty file
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")



