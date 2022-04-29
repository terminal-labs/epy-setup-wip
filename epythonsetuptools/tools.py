from pathlib import Path
from os import listdir
import importlib
import logging
import sys
import os

# logging.basicConfig(stream=sys.stderr, level=logging.INFO)
# logger = logging.getLogger()
# fh = logging.FileHandler('spam.log')
# logger.addHandler(fh)

def entrypoint(source, target, modpath):
    if source == "click" and target == "shell":
        return "[console_scripts]\n" + modpath

def setup(**kwargs):
    cwd = os.getcwd()
    files = listdir(cwd)

    dic = dict(**kwargs)

    for file in files:
        if "presetup.py" in file:
            presetup = importlib.import_module("presetup")
            additons = presetup.prep()
            for additon in additons:
                dic[additon["key"]] = additon["value"]
    return(dic)
