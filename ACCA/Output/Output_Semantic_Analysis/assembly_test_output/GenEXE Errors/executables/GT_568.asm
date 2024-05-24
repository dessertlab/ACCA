section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        or eax, 0xffffffff 
        not eax 
        push eax
        jmp myExitAddr