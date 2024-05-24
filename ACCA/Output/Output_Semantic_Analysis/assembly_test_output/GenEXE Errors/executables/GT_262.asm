section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        wrap_around:
        jmp myExitAddr