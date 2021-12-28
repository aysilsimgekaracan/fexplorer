from os import listdir, getcwd, chdir
from os.path import isfile, join, splitext, isdir, expanduser, dirname

def isDirectory(path): # Check if a given file path is a file or a directory
    if isdir(path):
        return True
    else:
        return False

def fileLabel(file, extension):
    label = f"{file}"
    return label

# find all files and folders in a given path
def getAllFilesInGivenDirectory(path):
	# files = [f for f in listdir(path) if isfile(join(path, f))]
    dirs = listdir(path)

    files =[]
    for file in dirs:
        filePath = path + "/" + file
        name, extension = splitext(filePath)
        if extension == "" and isDirectory(filePath) : extension = "dir"
        files.append({"name": file, "label": fileLabel(file, extension), "path": filePath, "type": extension})
        
    return files



def getCurrentDirectory():
    currentDirectory = getcwd()
    return currentDirectory

def getHomeDirectory(): # Users home address
    return expanduser('~')

def main():
    #print(f"Your current directory: {getCurrentDirectory()}")
    path = "/Users/aysilsimge/School/5. Dönem"
    # print(getAllFilesInGivenDirectory(path))
    #print(getHomeDirectory())
    print(goBackDirectory(path))

def goBackDirectory(path):
    return dirname(path)

if __name__ == "__main__":
    main()