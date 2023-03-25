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

def find_directory(directoryName, startingDirectory=None):

    # get root directory for the current OS
    if not startingDirectory:

        if os.name == 'nt':
            startingDirectory = os.environ['SystemDrive'] + '\\'
        else:
            startingDirectory = '/'

    for root, dirs, files in os.walk(startingDirectory):
        if directoryName in dirs:
            return os.path.join(root, directoryName)
    return directoryName


def CountScripts(directoryPath):
    countsByInterpreter = {}
    # Walk through the directory tree 
    for root, dirs, files in os.walk(directoryPath):
        for file in files:
            file_path = os.path.join(root, file)
            # Only count files with a ".sh" extension
            if file_path.endswith(".sh"):
                with open(file_path, "r") as f:
                    first_line = f.readline().strip()
                    interpreter = first_line[2:].strip()
                    countsByInterpreter[interpreter] = countsByInterpreter.get(
                        interpreter, 0) + 1
                    
    return countsByInterpreter

def PrintCounter(countsByInterpreter):
    for interpreter, count in countsByInterpreter.items():
        print(f"{interpreter}: {count}")


directoryName = input("Insert directory name: ")

try:
    directoryPath = (find_directory(directoryName))

except:
    print("The given directory wasn't found!")
    exit()  

countsByInterpreter = CountScripts(directoryPath)


PrintCounter(countsByInterpreter)



