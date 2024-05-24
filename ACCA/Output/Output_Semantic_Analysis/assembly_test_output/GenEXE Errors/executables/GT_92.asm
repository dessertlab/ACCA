section .data

dup2 equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        cmp cl, 0xff 
        jne dup2
        jmp myExitAddr