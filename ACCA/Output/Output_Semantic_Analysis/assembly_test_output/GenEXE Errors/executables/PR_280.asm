section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        xor edx, edx 
        mov byte [edx], 5
        jmp myExitAddr