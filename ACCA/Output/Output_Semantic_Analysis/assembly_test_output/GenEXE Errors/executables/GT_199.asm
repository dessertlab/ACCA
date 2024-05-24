section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        mov edi, 0x978cd092 
        mov ebx, edi
        jmp myExitAddr