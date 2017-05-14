def isVmFileName(fileName):
    fileExtension = fileName.split(".")[-1]
    if fileExtension == "vm":
        return True
    else:
        return False


def getFileAsListOfCommands(fileName, stringToSplitOn="\r\n"):
    commands = []
    fileObj = open(fileName)
    fileAsString = fileObj.read()
    linesOfFile = fileAsString.split(stringToSplitOn)
    for line in linesOfFile:
        appendLine = True
        # remove comments
        line = line.split("//")[0]
        # remove outer whitespace
        line = line.strip()
        # if a line is empty then don't include it
        # note that lines that originally had a comment would now be empty
        if line == "":
            appendLine = False
        if appendLine:
            commands.append(line)
    fileObj.close()
    return commands


def subValueIntoCommandList(commands, value):
    # make a copy of the list of commands
    commands = list(commands)
    for i in range(0, len(commands)):
        commands[i] = commands[i].format(value)
    return commands


def subValueDictIntoCommandList(commands, valueDict):
    # make a copy of the list of commands
    commands = list(commands)
    for i in range(0, len(commands)):
        commands[i] = commands[i].format(**valueDict)
    return commands
