section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        xor eax, eax 
        xor ebx, ebx 
        xor ecx, ecx 
        xor edx, edx
        jmp myExitAddr