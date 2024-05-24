section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        push ecx 
        mov ecx, 15
        jmp myExitAddr