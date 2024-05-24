section .data

l1 equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        pop ecx 
        dec ecx 
        jmp l1
        jmp myExitAddr