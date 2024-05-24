section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        mov al, byte [0xa4]
        jmp myExitAddr