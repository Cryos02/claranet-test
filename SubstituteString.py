#
#PREMISE#
"""
The following code assume that the user is looking for a directory
in the machine given only the name of it, I used my knowledge and the 
time given to research a suitable solution therefore I'm aware that the following 
code is not optimized and can result in logical errors as, for example, finding
the wrong directory in the presence of an homonym.
"""
#



import os
import sys

def find_directory(directoryName,startingDirectory=None):

    #get root directory for the current OS
    if not startingDirectory:
       
        if os.name == 'nt':
            startingDirectory = os.environ['SystemDrive'] + '\\'
        else:
            startingDirectory = '/'

    for root, dirs, files in os.walk(startingDirectory):
        if directoryName in dirs:
            return os.path.join(root, directoryName)
    return directoryName

def get_files_in_dir(directory):
    fileNames = []

    # get all files name in the selected directory
  
    for filename in os.listdir('.'):
        # Ignore hidden files
        if not filename.startswith('.'):
            fileNames.append(filename)
    return fileNames

def substitute_strings_in_files(stringToChange, changedString, fileNames, counter):

    #open and write in the files 
    with open(fileNames[counter], 'r') as file:
        content = file.read()
    content = content.replace(stringToChange, changedString)
    with open(fileNames[counter], 'w') as file:
        file.write(content)
    if(counter < len(fileNames) - 1):
        substitute_strings_in_files(stringToChange,changedString,fileNames,counter = counter+ 1)
    else:
        return None



directoryName = input("Insert directory name: ")

try:
    os.chdir(find_directory(directoryName))

except:
    print("The given directory wasn't found!")
    exit() 

filesName = get_files_in_dir(os.getcwd())

stringToChange = input("Word to change: ")
changedString = input("Word to change to: ")
counter = 0

substitute_strings_in_files(stringToChange,changedString,filesName,counter)



