section .data

l1 equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        pop ecx 
        loop l1 
        mov eax, 1
        jmp myExitAddr