section .data

_decode equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        jz _decode
        jmp myExitAddr