section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        marks dw 0, 0, 0, 0
        jmp myExitAddr