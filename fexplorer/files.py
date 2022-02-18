from os import listdir, getcwd, popen, rename, system
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
    
    allDetails = popen("ls -ld " + filePath + " | awk '{print $1, $2, $3, $4, $5, $6, $7, $8}'").read()
    return allDetails.rstrip("\n")

def renameFile(oldFilePath, newFilePath):
    rename(oldFilePath, newFilePath)

# find all files and folders in a given path
def getAllFilesInGivenDirectory(path):
    
	# files = [f for f in listdir(path) if isfile(join(path, f))]
	dirs = listdir(path)
	files =[]
 
	if len(dirs) != 0:
		max_lenght = max([len(d) for d in dirs]) + 10
	
		
		for file in dirs:
			if file[0] != ".":
				filePath = path + "/" + file
				name, extension = splitext(filePath)
				fileDetails = getFileDetails(filePath)
				if extension == "" and isDirectory(filePath) : extension = "folder"
				spaceLenght = max_lenght - len(file)
				icon = u"\U0001F4C1" if isDirectory(filePath) else "  "
				files.append({"name": file, "label": icon + " " + file + ' '*spaceLenght + fileDetails, "path": filePath, "type": extension, "fileDetails": fileDetails})

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

def changePermission(permisson_list, path):
	path = path.replace(" ", "\ ")
	path = path.replace("(", "\(")
	path = path.replace(")", "\)")
    
	permissions = ""
	for perms in permisson_list:
		sum = 0
		for p in perms:
			sum += p.get("val")
		permissions += str(sum)
	system(f"chmod {permissions} {path}")

# def main():
# 	#print(f"Your current directory: {getCurrentDirectory()}")
# 	path = "/Users/aysilsimge/"
# 	files = getAllFilesInGivenDirectory(path)
# 	for file in files:
# 		print(file)
# 	# print(getParentDirectory(path))
# 	# print(getFileDetails(path))

# def goBackDirectory(path):
#     return dirname(path)

# if __name__ == "__main__":
#     main()