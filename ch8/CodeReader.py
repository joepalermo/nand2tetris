from utilities import *

class CodeReader:

    def __init__(self, pathToVmFileName):

        self.vmFileName = pathToVmFileName.split("/")[-1]
        self.vmCommands = getFileAsListOfCommands(pathToVmFileName)
        self.numCommands = len(self.vmCommands)
        self.indexOfNextCommand = 0
        self.currentCommand = None

    def hasMoreCommands(self):
        return self.indexOfNextCommand < self.numCommands

    def getNextCommand(self):
        self.currentCommand = self.vmCommands[self.indexOfNextCommand]
        self.indexOfNextCommand += 1
        return self.currentCommand


def getCommandType(firstToken):
    if  firstToken in ["add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not"]:
        return "C_ARITHMETIC"
    elif firstToken == "push":
        return "C_PUSH"
    elif firstToken == "pop":
        return "C_POP"
    elif firstToken == "label":
        return "C_LABEL"
    elif firstToken == "goto":
        return "C_GOTO"
    elif firstToken == "if-goto":
        return "C_IF"
    elif firstToken == "function":
        return "C_FUNCTION"
    elif firstToken == "return":
        return "C_RETURN"
    elif firstToken == "call":
        return "C_CALL"
