from fexplorer.bestFileExplorer import cli
from fexplorer.files import getCurrentDirectory, isDirectory, getParentDirectory
import argparse
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", default=".", help="A filepath (. for the current directory)")
    args = parser.parse_args()
    args = vars(args)
    path = args.get("path")
    
    os.system('clear')
    
    if not isDirectory(path) or path == "." or path == "..":
        if path == ".":
            currentDirectory = getCurrentDirectory()
            cli(currentDirectory)
        elif path == "..":
            currentDirectory = getCurrentDirectory()
            parentDirectory = getParentDirectory(currentDirectory)
            cli(parentDirectory)
        else:
            print("Your path is not a valid directory")
    else:
        cli(path)
