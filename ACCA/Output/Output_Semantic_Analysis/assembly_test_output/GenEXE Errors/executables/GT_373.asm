section .data

shift_decode equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        xor cl, 0XAA 
        jz shift_decode
        jmp myExitAddr