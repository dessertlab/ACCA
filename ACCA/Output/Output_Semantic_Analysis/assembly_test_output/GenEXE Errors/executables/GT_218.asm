section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        mov byte [esp], 0x2f
        jmp myExitAddr