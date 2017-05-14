import sys
import os

def isVmFileName(fileName):
    fileExtension = fileName.split(".")[-1]
    if fileExtension == "vm":
        return True
    else:
        return False

if len(sys.argv) > 0:
    dirName = sys.argv[1]
    print dirName
    fileNames = [fileName for fileName in os.listdir(dirName) if isVmFileName(fileName)]

    print fileNames
