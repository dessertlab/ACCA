section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        ip equ 0x0100007f
        jmp myExitAddr