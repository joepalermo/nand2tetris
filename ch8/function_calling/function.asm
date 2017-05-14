({functionName})
@{numLocals}
D=A
({functionName}_ADD_LOCAL_VAR)
// test condition
@{functionName}_DONE_LOCAL_INIT
D;JEQ
// store remaining numLocals in R13
@R13
M=D
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// restore D to hold numLocals, but decrement
@R13
D=M-1
// jump to top of loop
@{functionName}_ADD_LOCAL_VAR
0;JMP
({functionName}_DONE_LOCAL_INIT)
