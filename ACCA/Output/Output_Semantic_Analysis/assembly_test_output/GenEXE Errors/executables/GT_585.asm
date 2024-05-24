section .data

do_inject equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        cmp BYTE al, 2 
        je do_inject
        jmp myExitAddr