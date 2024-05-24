section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        xor ecx, ecx 
        mul ecx
        jmp myExitAddr