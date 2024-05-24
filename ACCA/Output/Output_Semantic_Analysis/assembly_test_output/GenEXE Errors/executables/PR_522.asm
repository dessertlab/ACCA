section .data

trasnfer equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        push trasnfer 
        pop ecx
        jmp myExitAddr