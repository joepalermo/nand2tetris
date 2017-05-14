// push a numbered return address
@{functionName}_return_address_{numCallStatements}
D=A
@SP
M=M+1
A=M-1
M=D
// push the base address of the local segment
@LCL
D=M
@SP
M=M+1
A=M-1
M=D
// push the base address of the argument segment
@ARG
D=M
@SP
M=M+1
A=M-1
M=D
// push the base address of the this segment
@THIS
D=M
@SP
M=M+1
A=M-1
M=D
// push the base address of the that segment
@THAT
D=M
@SP
M=M+1
A=M-1
M=D
// set arg to new base of SP-numArgs-5
@SP
D=M
@{numArgs}
D=D-A
@5
D=D-A
@ARG
M=D
// set LCL to top of the stack
@SP
D=M
@LCL
M=D
// goto f
@{functionName}
0;JMP
// declare a label for the return address
({functionName}_return_address_{numCallStatements})
