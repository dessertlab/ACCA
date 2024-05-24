section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        cmp cl, 0x11 
        jl 0xff 
        add dl, 0x5
        jmp myExitAddr