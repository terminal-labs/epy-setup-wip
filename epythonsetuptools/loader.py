import importlib
import importlib.machinery
from pathlib import Path
from os import listdir

def cfp(path):
    return Path(path).resolve().parent

def getmode(BASE_DIR, name, package):
    files = listdir(BASE_DIR)
    for file in files:
        if file.endswith(".so") and name in file:
            return importlib.import_module(package + "." + name, package=package)
    source_file = str(BASE_DIR) + "/" + name + ".py"
    loader = importlib.machinery.SourceFileLoader("functions", source_file)
    module = loader.load_module()
    return module
