section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        push 0x37333333 
        push 0x3170762d
        jmp myExitAddr