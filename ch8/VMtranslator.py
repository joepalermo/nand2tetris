import sys
import os

from CodeReader import *
from CodeWriter import *
from utilities import *


dirName = sys.argv[1]
vmFileNames = [fileName for fileName in os.listdir(dirName) if isVmFileName(fileName)]
readers = [CodeReader(dirName + "/" + fileName) for fileName in vmFileNames]

asmFileName = dirName.split("/")[-1] + ".asm"
writer = CodeWriter(dirName + "/" + asmFileName)
writer.writeInit()

for reader in readers:
    writer.setCurrentFileName(reader.vmFileName)
    while(reader.hasMoreCommands()):
        currentCommand = reader.getNextCommand()
        commandTokens = currentCommand.split()
        commandType = getCommandType(commandTokens[0])
        if commandType == "C_ARITHMETIC":
            writer.writeArithmetic(currentCommand)
        elif commandType == "C_PUSH" or commandType == "C_POP":
            segment = commandTokens[1]
            index = commandTokens[2]
            writer.writePushPop(commandType, segment, index)
        elif commandType == "C_LABEL":
            label = commandTokens[1]
            writer.writeLabel(label)
        elif commandType == "C_GOTO":
            label = commandTokens[1]
            writer.writeGoto(label)
        elif commandType == "C_IF":
            label = commandTokens[1]
            writer.writeIf(label)
        elif commandType == "C_CALL":
            functionName = commandTokens[1]
            numArgs = commandTokens[2]
            writer.writeCall(functionName, numArgs)
        elif commandType == "C_RETURN":
            writer.writeReturn()
        elif commandType == "C_FUNCTION":
            functionName = commandTokens[1]
            numLocals = commandTokens[2]
            # set current function name so that it can be included in labels
            writer.setCurrentFunctionName(functionName)
            writer.writeFunction(functionName, numLocals)

writer.close()
