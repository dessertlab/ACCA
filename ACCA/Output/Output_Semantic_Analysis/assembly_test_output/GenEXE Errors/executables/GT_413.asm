section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        mov cl,0x2
        jmp myExitAddr