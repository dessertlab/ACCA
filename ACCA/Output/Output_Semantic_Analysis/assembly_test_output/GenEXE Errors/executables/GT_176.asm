section .data

lowbound equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        cmp BYTE [esi], 0x7 
        jle lowbound
        jmp myExitAddr