section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        push 0x978cd092 
        pop edi 
        pop ebx
        jmp myExitAddr