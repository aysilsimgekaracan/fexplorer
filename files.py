from os import listdir, getcwd
from os.path import isfile, join, splitext, isdir

def isDirectory(path): # Check if a given file path is a file or a directory
	if isdir(path):
	    return True
	else:
		return False

def fileLabel(file, extension):
	# icon = ""
	# if extension == "folder":
	# 	icon = u"\U0001F4C1"
	# elif extension == ".png":
	# 	icon = u"\U0001F5BC"
	# elif extension == ".txt" or extension == ".text":
	# 	icon = u"\U0001F5B9"
	# elif extension == ".doc" or extension == ".docx" or extension == ".pdf":
	# 	icon = u"\U0001F5BA"
	# else:
	# 	icon = u"\u003F"

	label = f"{file}"
	return label


def getAllFilesInGivenDirectory(path):
	# files = [f for f in listdir(path) if isfile(join(path, f))]
	dirs = listdir(path)

	files =[]
	for file in dirs:
		filePath = path + "/" + file
		name, extension = splitext(filePath)
		if extension == "" and isDirectory(filePath) : extension = "folder"
		files.append({"name": file, "label": fileLabel(file, extension), "path": filePath, "type": extension})


	return files



def getCurrentDirectory():
	currentDirectory = getcwd()
	return currentDirectory

def main():
	#print(f"Your current directory: {getCurrentDirectory()}")
	path = "/Users/aysilsimge/School/5. Dönem"
	listFiles(getAllFilesInGivenDirectory(path))


if __name__ == "__main__":
    main()