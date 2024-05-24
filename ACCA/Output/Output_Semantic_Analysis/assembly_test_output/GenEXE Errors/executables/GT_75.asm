section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        push word 0x3582
        jmp myExitAddr