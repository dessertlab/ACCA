section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        cmp eax, dword [edi] 
        not dword [edi]
        jmp myExitAddr