section .data

write equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        test eax, eax 
        jz write 
        xor eax, eax
        jmp myExitAddr