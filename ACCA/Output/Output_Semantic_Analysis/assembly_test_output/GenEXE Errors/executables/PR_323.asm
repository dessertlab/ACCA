section .data

shellcode equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        cmp bl, 0xaa 
        jz shellcode
        jmp myExitAddr