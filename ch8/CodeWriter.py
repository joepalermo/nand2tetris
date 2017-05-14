import os

from utilities import *

class CodeWriter:

    def __init__(self, asmFileName):
        self.asmFile = open(asmFileName, "w")
        self.numEqStatements = 0
        self.numGtStatements = 0
        self.numLtStatements = 0
        self.numCallStatements = 0
        self.currentFunctionName = None
        self.assemblyDict = self.initializeAssemblyDict()

    def getCurrentFunctionName(self):
        return self.currentFunctionName

    def setCurrentFunctionName(self, functionName):
        self.currentFunctionName = functionName

    def getCurrentFileName(self):
        return self.currentFileName

    def setCurrentFileName(self, fileName):
        self.currentFileName = fileName

    def initializeAssemblyDict(self):
        assemblyDict = {}
        assemblyChunkDirNames = ["arithmetic", "memory_access",
        "program_flow", "function_calling", "init"]
        for dirName in assemblyChunkDirNames:
            for fileName in os.listdir(dirName):
                pathString = dirName + "/" + fileName
                commandList = getFileAsListOfCommands(pathString, stringToSplitOn="\n")
                commandSubType = fileName.split(".")[0]
                assemblyDict[commandSubType] = commandList
        return assemblyDict

    def close(self):
        self.asmFile.close()

    def writeLines(self, lines):
        for line in lines:
            self.asmFile.write(line + "\n")

    # write arithmetic commands
    def writeArithmetic(self, command):
        if command == "add":
            self.writeLines(self.assemblyDict["add"])
        elif command == "sub":
            self.writeLines(self.assemblyDict["sub"])
        elif command == "neg":
            self.writeLines(self.assemblyDict["neg"])
        elif command == "and":
            self.writeLines(self.assemblyDict["and"])
        elif command == "or":
            self.writeLines(self.assemblyDict["or"])
        elif command == "not":
            self.writeLines(self.assemblyDict["not"])

        elif command == "eq":
            self.numEqStatements += 1
            self.writeLines(subValueIntoCommandList(self.assemblyDict["eq"],
                                                    self.numEqStatements))
        elif command == "gt":
            self.numGtStatements += 1
            self.writeLines(subValueIntoCommandList(self.assemblyDict["gt"],
                                                    self.numGtStatements))
        elif command == "lt":
            self.numLtStatements += 1
            self.writeLines(subValueIntoCommandList(self.assemblyDict["lt"],
                                                    self.numLtStatements))


    # write push/pop commands
    def writePushPop(self, commandType, segment, index):
        if commandType == "C_PUSH" and segment == "constant":
            self.writeLines(subValueIntoCommandList(self.assemblyDict["push_constant"], index))

        elif commandType == "C_PUSH" and segment == "local":
            self.writeLines(subValueIntoCommandList(self.assemblyDict["push_local"], index))

        elif commandType == "C_PUSH" and segment == "argument":
            self.writeLines(subValueIntoCommandList(self.assemblyDict["push_argument"], index))

        elif commandType == "C_PUSH" and segment == "this":
            self.writeLines(subValueIntoCommandList(self.assemblyDict["push_this"], index))

        elif commandType == "C_PUSH" and segment == "that":
            self.writeLines(subValueIntoCommandList(self.assemblyDict["push_that"], index))

        elif commandType == "C_PUSH" and segment == "pointer":
            self.writeLines(subValueIntoCommandList(self.assemblyDict["push_pointer"], index))

        elif commandType == "C_PUSH" and segment == "temp":
            self.writeLines(subValueIntoCommandList(self.assemblyDict["push_temp"], index))

        elif commandType == "C_PUSH" and segment == "static":
            valueDict = {"fileName": self.getCurrentFileName(),
                         "index": index}
            self.writeLines(subValueDictIntoCommandList(self.assemblyDict["push_static"], valueDict))


        elif commandType == "C_POP" and segment == "local":
            self.writeLines(subValueIntoCommandList(self.assemblyDict["pop_local"], index))

        elif commandType == "C_POP" and segment == "argument":
            self.writeLines(subValueIntoCommandList(self.assemblyDict["pop_argument"], index))

        elif commandType == "C_POP" and segment == "this":
            self.writeLines(subValueIntoCommandList(self.assemblyDict["pop_this"], index))

        elif commandType == "C_POP" and segment == "that":
            self.writeLines(subValueIntoCommandList(self.assemblyDict["pop_that"], index))

        elif commandType == "C_POP" and segment == "pointer":
            self.writeLines(subValueIntoCommandList(self.assemblyDict["pop_pointer"], index))

        elif commandType == "C_POP" and segment == "temp":
            self.writeLines(subValueIntoCommandList(self.assemblyDict["pop_temp"], index))

        elif commandType == "C_POP" and segment == "static":
            valueDict = {"fileName": self.getCurrentFileName(),
                         "index": index}
            self.writeLines(subValueDictIntoCommandList(self.assemblyDict["pop_static"], valueDict))

    def writeInit(self):
        self.writeLines(self.assemblyDict["init"])

    def writeLabel(self, label):
        if self.getCurrentFunctionName() != None:
            label = self.getCurrentFunctionName() + "$" + label
        self.writeLines(subValueIntoCommandList(self.assemblyDict["label"], label))

    def writeGoto(self, label):
        if self.getCurrentFunctionName() != None:
            label = self.getCurrentFunctionName() + "$" + label
        self.writeLines(subValueIntoCommandList(self.assemblyDict["goto"], label))

    def writeIf(self, label):
        if self.getCurrentFunctionName() != None:
            label = self.getCurrentFunctionName() + "$" + label
        self.writeLines(subValueIntoCommandList(self.assemblyDict["if"], label))

    def writeCall(self, functionName, numArgs):
        self.numCallStatements += 1
        valueDict = {"functionName": functionName,
                     "numArgs": numArgs,
                     "numCallStatements": self.numCallStatements}
        self.writeLines(subValueDictIntoCommandList(self.assemblyDict["call"], valueDict))

    def writeReturn(self):
        self.writeLines(self.assemblyDict["return"])

    def writeFunction(self, functionName, numLocals):
        valueDict = {"functionName": functionName, "numLocals": numLocals}
        self.writeLines(subValueDictIntoCommandList(self.assemblyDict["function"], valueDict))
