from os import listdir, getcwd, popen
from os.path import splitext, isdir, expanduser
from pathlib import Path
import subprocess

def isDirectory(path): # Check if a given file path is a file or a directory
	if isdir(path):
		return True
	else:
		return False

# def fileLabel(file, extension):
#     label = f"{file}"
#     return label

def getFileDetails(filePath):
    filePath = filePath.replace(" ", "\ ")
    filePath = filePath.replace("(", "\(")
    filePath = filePath.replace(")", "\)")
    
    output = popen("ls -ld " + filePath + " | awk '{print $1, $2, $3, $4, $5, $6, $7, $8}'").read()
    return output

# find all files and folders in a given path
def getAllFilesInGivenDirectory(path):
    
	# files = [f for f in listdir(path) if isfile(join(path, f))]
	dirs = listdir(path)
	
	max_lenght = max([len(d) for d in dirs]) + 20
 
	files =[]
	for file in dirs:
		filePath = path + "/" + file
		name, extension = splitext(filePath)
		fileDetails = getFileDetails(filePath)
		spaceLenght = max_lenght - len(file)
		if extension == "" and isDirectory(filePath) : extension = "folder"
		files.append({"name": file, "label": file + ' '*spaceLenght + fileDetails, "path": filePath, "type": extension, "fileDetails": fileDetails})

	# Add Parent Directory
	parentPath = getParentDirectory(path)
	files.append({"name": "Parent Directory", "label": "[Back]", "path": parentPath, "type": "folder"})
 
	# Add An Option to Quit
	files.append({"label": "[Quit]", "type": "quit"})
	return files

# Go one directory back
def getParentDirectory(givenPath): 
    p = Path(givenPath)
    return str(p.parent)


def getCurrentDirectory():
    currentDirectory = getcwd()
    return currentDirectory

def getHomeDirectory(): # Users home address
    return expanduser('~')

def main():
    	#print(f"Your current directory: {getCurrentDirectory()}")
	path = "/Users/aysilsimge/School/5. Dönem"
	# print(getAllFilesInGivenDirectory(path))
	# print(getParentDirectory(path))
	# print(getFileDetails(path))

# def goBackDirectory(path):
#     return dirname(path)

if __name__ == "__main__":
    main()