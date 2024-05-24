section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        mov byte [eax], 0x1
        jmp myExitAddr