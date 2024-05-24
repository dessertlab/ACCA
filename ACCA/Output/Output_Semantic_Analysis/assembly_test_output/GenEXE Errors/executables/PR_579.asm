section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        mov edx, 0x65676760
        jmp myExitAddr