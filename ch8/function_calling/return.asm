@LCL
D=M
@13
M=D // FRAME = LCL

@5
D=D-A
A=D
D=M
@14
M=D // RETADDR = *(FRAME - 5)

@SP
M=M-1
A=M
D=M // pop into D

@ARG
A=M
M=D // *ARG = pop()

@ARG
D=M+1 // D = ARG+1
@SP
M=D // SP = ARG+1

@1
D=A
@13
D=M-D
A=D
D=M
@THAT
M=D // THAT = *(FRAME-1)

@2
D=A
@13
D=M-D
A=D
D=M
@THIS
M=D // THIS = *(FRAME-2)

@3
D=A
@13
D=M-D
A=D
D=M
@ARG
M=D // ARG = *(FRAME-3)

@4
D=A
@13
D=M-D
A=D
D=M
@LCL
M=D // LCL = *(FRAME-4)

@14
A=M
0;JMP // goto RETADDR
