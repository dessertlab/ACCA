section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        decoder: 
        pop esi 
        mov edi, esi
        jmp myExitAddr