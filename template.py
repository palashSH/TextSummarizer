import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:  %(messages)s:')
projectname = 'textSummarizer'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src{projectname}/__init__.py",
    f"src{projectname}/components/__init__.py",
    f"src{projectname}/utils/__init__.py",
    f"src{projectname}/utils/common.py",
    f"src{projectname}/logging/__init__.py",
    f"src{projectname}/config/__init__.py",
    f"src{projectname}/config/configuration.py",
    f"src{projectname}/pipeline/__init__.py",
    f"src{projectname}/entity/__init__.py",
    f"src{projectname}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for file in list_of_files:
    file_path = Path(file)  
    file_dir, file_name = os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Created directory: {file_dir} for the file {file_name}")

    if not os.path.exists(file_path) or os.path.getsize == 0:
        with open(file_path, 'w'):
            pass
        logging.info(f"Created empty file: {file_name} in path {file_path}") 
    else:
        logging.info(f"File {file_name} already exists.")