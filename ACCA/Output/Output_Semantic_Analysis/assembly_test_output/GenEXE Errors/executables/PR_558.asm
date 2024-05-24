section .data

l1 equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        cmp DWORD [eax], edi 
        jne l1
        jmp myExitAddr